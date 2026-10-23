#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成并合并沪教版高中（十至十二年级）数学知识图谱。

用法：
  python3 _builder/build_high.py            # 合并进 data/*.json
  python3 _builder/build_high.py --dry-run  # 只打印统计，不写文件

行为：
1) 从 _builder/hcontent/ 下的 6 个模块（高一上/下 … 高三上/下）收集知识点；
2) 删除 data/ 中已有的十至十二年级数学内容（保证可重复运行）；
3) 追加新知识点、先修边、题目，并写出
   data/cn-highschool-curriculum-standards.json。

小学（1—5 年级）与初中（6—9 年级）的内容不会被改动；
英语知识点（grade 为字符串）同样不受影响。
"""
import argparse
import importlib
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import high_standards  # noqa: E402

MODULES = ["h1a", "h1b", "h2a", "h2b", "h3a", "h3b"]
DATA = os.path.join(ROOT, "data")
TOPICS = os.path.join(DATA, "topics.json")
DEPS = os.path.join(DATA, "dependencies.json")
QUESTIONS = os.path.join(DATA, "questions.json")
HSTANDARDS = os.path.join(DATA, "cn-highschool-curriculum-standards.json")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def collect():
    topics, prereqs, questions = [], [], []
    for name in MODULES:
        mod = importlib.import_module("hcontent." + name)
        for pack in mod.TOPICS:
            topics.append(pack["topic"])
            prereqs.append((pack["topic"]["id"], pack["prereqs"]))
            questions.extend(pack["questions"])
    return topics, prereqs, questions


def is_high(t):
    """高中（10—12 年级）数学知识点；英语知识点靠 subject 区分，不受影响。"""
    return (not t.get("external")
            and t.get("subject") != "english"
            and isinstance(t.get("grade"), int)
            and t["grade"] >= 10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    new_topics, new_prereqs, new_questions = collect()

    ids = [t["id"] for t in new_topics]
    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        sys.exit("知识点 id 重复：%s" % "、".join(sorted(dup)))

    old_topics = load(TOPICS)
    # 十至十二年级的旧内容会被整体替换，不参与冲突检查
    old_ids = {t["id"] for t in old_topics if not is_high(t)}
    clash = sorted(set(ids) & old_ids)
    if clash:
        sys.exit("知识点 id 与现有数据冲突：%s" % "、".join(clash))

    name_of = {t["id"]: t["name"] for t in old_topics + new_topics}
    deps = []
    seen = set()
    for tid, pres in new_prereqs:
        for pid, strength in pres:
            if pid not in name_of:
                sys.exit("%s 的先修 %s 不存在" % (tid, pid))
            if (tid, pid) in seen:
                sys.exit("重复先修边：%s → %s" % (tid, pid))
            seen.add((tid, pid))
            deps.append({
                "topicId": tid,
                "prerequisiteId": pid,
                "strength": strength,
                "reason": "「%s」的学习以「%s」为基础。" % (name_of[tid], name_of[pid]),
            })

    keep_topics = [t for t in old_topics if not is_high(t)]
    keep_ids = {t["id"] for t in keep_topics}
    keep_deps = [d for d in load(DEPS) if d["topicId"] in keep_ids and d["prerequisiteId"] in keep_ids]
    keep_qs = [q for q in load(QUESTIONS) if q["topicId"] in keep_ids]

    topics = keep_topics + new_topics
    deps = keep_deps + deps
    # 数学题按 id 排序；英语题保持原顺序（英语由 build_english.py 负责排序），互不干扰
    math_qs = keep_qs + new_questions
    math_qs.sort(key=lambda q: (int(q["topicId"].split("_")[1]), int(q["id"].rsplit("_q", 1)[1])))
    eng_qs = [q for q in load(QUESTIONS) if not q["topicId"].startswith("cnm_")]
    questions = math_qs + eng_qs

    print("新增知识点 %d（高一上 %d、高一下 %d、高二上 %d、高二下 %d、高三上 %d、高三下 %d）" % (
        len(new_topics),
        *[sum(1 for t in new_topics if t["grade"] == g and t["semester"] == s)
          for g in (10, 11, 12) for s in ("上", "下")]))
    print("新增先修边 %d（hard %d，soft %d）" % (
        len(deps) - len(keep_deps),
        sum(1 for d in deps if d["topicId"] not in keep_ids and d["strength"] == "hard"),
        sum(1 for d in deps if d["topicId"] not in keep_ids and d["strength"] == "soft")))
    print("新增题目 %d；知识点合计 %d（正式 %d），题目合计 %d" % (
        len(new_questions), len(topics), sum(1 for t in topics if not t["external"]), len(questions)))
    print("按类型：%s" % dict(Counter(q["type"] for q in new_questions)))

    counts = Counter(q["topicId"] for q in new_questions)
    for t in new_topics:
        if counts[t["id"]] < 3:
            sys.exit("%s(%s) 只有 %d 道题" % (t["id"], t["name"], counts[t["id"]]))

    if args.dry_run:
        return

    items = []
    for sid, domain, theme, section, clause, text in high_standards.ITEMS:
        items.append({
            "id": "cmh-2017:" + sid,
            "stage": "必修" if sid.startswith("1.") else "选择性必修",
            "domain": domain,
            "theme": theme,
            "section": section,
            "clause": clause,
            "text": text,
            "page_or_ref": "待核",
            "verbatim": False,
        })
    dump(HSTANDARDS, {"source": high_standards.SOURCE, "items": items})
    dump(TOPICS, topics)
    dump(DEPS, deps)
    dump(QUESTIONS, questions)
    print("已写入 data/topics.json、data/dependencies.json、data/questions.json、"
          "data/cn-highschool-curriculum-standards.json")
    cited = {s["id"] for t in new_topics for s in t["standards"]}
    print("课标条目 %d 条，被高中知识点引用 %d 条；未被引用的：%s" % (
        len(items), len(cited), "、".join(sorted({i["id"] for i in items} - cited)) or "无"))


if __name__ == "__main__":
    main()
