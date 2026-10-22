#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成并合并沪教版英语（三至九年级）知识图谱。

用法：
  python3 _builder/build_english.py            # 合并进 data/*.json
  python3 _builder/build_english.py --dry-run  # 只打印统计，不写文件

行为：
1) 从 _builder/econtent/ 下的 7 个模块（三上/下 … 九上/下）收集知识点；
2) 删除 data/ 中已有的英语内容（subject == "english"），保证可重复运行；
3) 追加英语知识点、先修边、题目，并写出 data/cn-english-curriculum-standards.json。

数学数据（小学 1—5、初中 6—9）不会被改动，英语与数学之间不连先修边。
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

import estandards  # noqa: E402

MODULES = ["e3", "e4", "e5", "e6", "e7", "e8", "e9"]
DATA = os.path.join(ROOT, "data")
TOPICS = os.path.join(DATA, "topics.json")
DEPS = os.path.join(DATA, "dependencies.json")
QUESTIONS = os.path.join(DATA, "questions.json")
ESTANDARDS = os.path.join(DATA, "cn-english-curriculum-standards.json")

MIN_QUESTIONS = 4


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
        mod = importlib.import_module("econtent." + name)
        for pack in mod.TOPICS:
            topics.append(pack["topic"])
            prereqs.append((pack["topic"]["id"], pack["prereqs"]))
            questions.extend(pack["questions"])
    return topics, prereqs, questions


def is_english(t):
    return t.get("subject") == "english"


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
    old_ids = {t["id"] for t in old_topics if not is_english(t)}
    clash = sorted(set(ids) & old_ids)
    if clash:
        sys.exit("知识点 id 与数学数据冲突：%s" % "、".join(clash))

    # 英语课标条目
    items = []
    std_ids = set()
    for sid, stage, domain, theme, text in estandards.ITEMS:
        full = "ces-2022:" + sid
        if full in std_ids:
            sys.exit("课标条目 id 重复：%s" % full)
        std_ids.add(full)
        items.append({
            "id": full,
            "stage": stage,
            "domain": domain,
            "theme": theme,
            "text": text,
            "page_or_ref": "待核",
            "verbatim": False,
        })

    name_of = {t["id"]: t["name"] for t in old_topics + new_topics}
    deps = []
    seen = set()
    for tid, pres in new_prereqs:
        for pid, strength in pres:
            if pid not in name_of:
                sys.exit("%s 的先修 %s 不存在" % (tid, pid))
            if pid in old_ids:
                sys.exit("%s 的先修 %s 指向数学知识点（英语单独成图）" % (tid, pid))
            if (tid, pid) in seen:
                sys.exit("重复先修边：%s → %s" % (tid, pid))
            seen.add((tid, pid))
            deps.append({
                "topicId": tid,
                "prerequisiteId": pid,
                "strength": strength,
                "reason": "「%s」的学习以「%s」为基础。" % (name_of[tid], name_of[pid]),
            })

    missing_std = sorted({s["id"] for t in new_topics for s in t["standards"]} - std_ids)
    if missing_std:
        sys.exit("引用了不存在的课标条目：%s" % "、".join(missing_std))

    keep_topics = [t for t in old_topics if not is_english(t)]
    keep_ids = {t["id"] for t in keep_topics}
    keep_deps = [d for d in load(DEPS) if d["topicId"] in keep_ids]
    keep_qs = [q for q in load(QUESTIONS) if q["topicId"] in keep_ids]

    order = {t["id"]: i for i, t in enumerate(new_topics)}
    topics = keep_topics + new_topics
    deps = keep_deps + deps
    questions = keep_qs + sorted(
        new_questions, key=lambda q: (order[q["topicId"]], int(q["id"].rsplit("_q", 1)[1])))

    print("新增英语知识点 %d 个" % len(new_topics))
    for g in range(3, 10):
        up = sum(1 for t in new_topics if t["grade"] == g and t["semester"] == "上")
        down = sum(1 for t in new_topics if t["grade"] == g and t["semester"] == "下")
        print("  %d 年级：上 %d、下 %d" % (g, up, down))
    print("新增先修边 %d（hard %d，soft %d）" % (
        len(deps) - len(keep_deps),
        sum(1 for d in deps if d["topicId"] in order and d["strength"] == "hard"),
        sum(1 for d in deps if d["topicId"] in order and d["strength"] == "soft")))
    print("新增题目 %d（%s）" % (len(new_questions), dict(Counter(q["type"] for q in new_questions))))
    print("知识点合计 %d，题目合计 %d" % (len(topics), len(questions)))

    per_topic = Counter(q["topicId"] for q in new_questions)
    for t in new_topics:
        n = per_topic.get(t["id"], 0)
        if n < MIN_QUESTIONS:
            sys.exit("%s(%s) 只有 %d 道题，至少需要 %d 道" % (t["id"], t["name"], n, MIN_QUESTIONS))
        diffs = {q["difficulty"] for q in new_questions if q["topicId"] == t["id"]}
        if not {"basic", "standard"} <= diffs:
            sys.exit("%s(%s) 的难度需同时含 basic 与 standard" % (t["id"], t["name"]))
    cited = {s["id"] for t in new_topics for s in t["standards"]}
    print("课标条目 %d 条，被引用 %d 条；未被引用：%s" % (
        len(items), len(cited), "、".join(sorted(std_ids - cited)) or "无"))

    if args.dry_run:
        return

    dump(ESTANDARDS, {"source": estandards.SOURCE, "items": items})
    dump(TOPICS, topics)
    dump(DEPS, deps)
    dump(QUESTIONS, questions)
    print("已写入 data/topics.json、data/dependencies.json、data/questions.json、"
          "data/cn-english-curriculum-standards.json")


if __name__ == "__main__":
    main()
