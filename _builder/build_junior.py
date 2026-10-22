#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成并合并沪教版初中（六至九年级）知识图谱。

用法：
  python3 _builder/build_junior.py            # 合并进 data/*.json
  python3 _builder/build_junior.py --dry-run  # 只打印统计，不写文件

行为：
1) 从 _builder/jcontent/ 下的 8 个模块（六上/下 … 九上/下）收集知识点；
2) 删除 data/ 中已有的六至九年级内容（保证可重复运行）；
3) 追加新知识点、先修边、题目，并写出 data/cn-junior-curriculum-standards.json。

小学段（1—5 年级）的 data 内容不会被改动。
"""
import argparse
import importlib
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import junior_standards  # noqa: E402

MODULES = ["j6a", "j6b", "j7a", "j7b", "j8a", "j8b", "j9a", "j9b"]
DATA = os.path.join(ROOT, "data")
TOPICS = os.path.join(DATA, "topics.json")
DEPS = os.path.join(DATA, "dependencies.json")
QUESTIONS = os.path.join(DATA, "questions.json")
JSTANDARDS = os.path.join(DATA, "cn-junior-curriculum-standards.json")


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
        mod = importlib.import_module("jcontent." + name)
        for pack in mod.TOPICS:
            topics.append(pack["topic"])
            prereqs.append((pack["topic"]["id"], pack["prereqs"]))
            questions.extend(pack["questions"])
    return topics, prereqs, questions


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
    # 六至九年级的旧内容会被整体替换，不参与冲突检查
    old_ids = {t["id"] for t in old_topics
               if t.get("external") or not isinstance(t.get("grade"), int) or t["grade"] <= 5}
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

    keep_topics = [t for t in old_topics if t.get("external") or not isinstance(t.get("grade"), int) or t["grade"] <= 5]
    keep_ids = {t["id"] for t in keep_topics}
    keep_deps = [d for d in load(DEPS) if d["topicId"] in keep_ids and d["prerequisiteId"] in keep_ids]
    keep_qs = [q for q in load(QUESTIONS) if q["topicId"] in keep_ids]

    topics = keep_topics + new_topics
    deps = keep_deps + deps
    questions = keep_qs + new_questions
    questions.sort(key=lambda q: (int(q["topicId"].split("_")[1]), int(q["id"].rsplit("_q", 1)[1])))

    print("新增知识点 %d（六上 %d、六下 %d、七上 %d、七下 %d、八上 %d、八下 %d、九上 %d、九下 %d）" % (
        len(new_topics),
        *[sum(1 for t in new_topics if t["grade"] == g and t["semester"] == s)
          for g in (6, 7, 8, 9) for s in ("上", "下")]))
    print("新增先修边 %d（hard %d，soft %d）" % (
        len(deps) - len(keep_deps),
        sum(1 for d in deps if d["topicId"] not in keep_ids and d["strength"] == "hard"),
        sum(1 for d in deps if d["topicId"] not in keep_ids and d["strength"] == "soft")))
    print("新增题目 %d；知识点合计 %d（正式 %d），题目合计 %d" % (
        len(new_questions), len(topics), sum(1 for t in topics if not t["external"]), len(questions)))
    print("按类型：%s" % dict(Counter(q["type"] for q in new_questions)))
    missing = [q["topicId"] for q in new_questions]
    for t in new_topics:
        n = missing.count(t["id"])
        if n < 3:
            sys.exit("%s(%s) 只有 %d 道题" % (t["id"], t["name"], n))

    if args.dry_run:
        return

    items = []
    for sid, domain, theme, section, clause, text in junior_standards.ITEMS:
        items.append({
            "id": "cms-2022:" + sid,
            "domain": domain,
            "theme": theme,
            "section": section,
            "clause": clause,
            "text": text,
            "page_or_ref": "待核",
            "verbatim": False,
        })
    dump(JSTANDARDS, {"source": junior_standards.SOURCE, "items": items})
    dump(TOPICS, topics)
    dump(DEPS, deps)
    dump(QUESTIONS, questions)
    print("已写入 data/topics.json、data/dependencies.json、data/questions.json、data/cn-junior-curriculum-standards.json")
    cited = {s["id"] for t in new_topics for s in t["standards"]}
    print("课标条目 %d 条，被初中知识点引用 %d 条；未被引用的：%s" % (
        len(items), len(cited), "、".join(sorted({i["id"] for i in items} - cited)) or "无"))


if __name__ == "__main__":
    main()
