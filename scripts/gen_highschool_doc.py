#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 data/topics.json 生成 docs/highschool-chapters.md（高中数学册次 / 章 / 小节清单）。

用法：python3 scripts/gen_highschool_doc.py
"""

import json
import os
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS = os.path.join(ROOT, "data", "topics.json")
OUT = os.path.join(ROOT, "docs", "highschool-chapters.md")

BOOK_ORDER = [("必修第一册", "高一上"), ("必修第二册", "高一下"), ("必修第三册", "高二上"),
              ("选择性必修第一册", "高二下"), ("选择性必修第二册", "高三上"),
              ("选择性必修第三册", "高三下")]
GRADE_ZH = {10: "高一", 11: "高二", 12: "高三"}


def main():
    topics = json.load(open(TOPICS, encoding="utf-8"))
    hs = [t for t in topics
          if not t.get("external") and (t.get("subject") or "math") == "math" and t["grade"] >= 10]

    by_book = OrderedDict((b, []) for b, _ in BOOK_ORDER)
    for t in hs:
        by_book.setdefault(t["chapter"].split(" ", 1)[0], []).append(t)

    lines = []
    add = lines.append
    add("# 高中数学（必修 + 选择性必修，沪教版）章节目录与知识点清单")
    add("")
    add("> 由 `python3 scripts/gen_highschool_doc.py` 从 `data/topics.json` 自动生成；"
        "共 **%d 个知识点**，覆盖必修第一至第三册、选择性必修第一至第三册。" % len(hs))
    add("> 教材：沪教版《数学》（上海教育出版社，2020 年审定）。章节目录以公开教材目录整理，"
        "**未与课本逐页核对**，教师使用前请以课本为准；必修第四册与选择性必修第三册以数学建模活动为主，"
        "本版只在选择性必修第三册设 4 个建模知识点。")
    add("")
    add("| 册次 | 年级学期 | 知识点 | id 区间 |")
    add("|---|---|---:|---|")
    for book, sem in BOOK_ORDER:
        ts = by_book.get(book) or []
        if not ts:
            continue
        add("| %s | %s | %d | `%s` – `%s` |" % (book, sem, len(ts), ts[0]["id"], ts[-1]["id"]))
    add("| **合计** | | **%d** | |" % len(hs))
    add("")

    for book, sem in BOOK_ORDER:
        ts = by_book.get(book) or []
        if not ts:
            continue
        add("## %s（%s）" % (book, sem))
        add("")
        chapters = OrderedDict()
        for t in ts:
            parts = t["chapter"].split(" ")
            key = (parts[1], parts[2])
            chapters.setdefault(key, OrderedDict()).setdefault(" ".join(parts[3:]), []).append(t)
        for (no, name), sections in chapters.items():
            add("### %s %s" % (no, name))
            add("")
            for section, items in sections.items():
                add("- **%s**" % (section or name))
                for t in items:
                    stds = "、".join(s["id"].split(":", 1)[-1] for s in t.get("standards", []))
                    add("  - %s（`%s`；课标 %s）" % (t["name"], t["id"], stds or "—"))
            add("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print("已写入 %s（%d 个知识点）" % (OUT, len(hs)))


if __name__ == "__main__":
    main()
