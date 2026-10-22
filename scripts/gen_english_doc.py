#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 data/topics.json 生成 docs/english-chapters.md（英语册次 / Unit / 册末卷清单）。

用法：python3 scripts/gen_english_doc.py
"""

import json
import os
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS = os.path.join(ROOT, "data", "topics.json")
OUT = os.path.join(ROOT, "docs", "english-chapters.md")

BOOK_ORDER = ["三年级上", "三年级下", "四年级上", "四年级下", "五年级上", "五年级下",
              "六年级上", "六年级下", "七年级上", "七年级下", "八年级上", "八年级下",
              "九年级上", "九年级下", "必修第一册", "必修第二册", "必修第三册",
              "选择性必修第一册", "选择性必修第二册", "选择性必修第三册", "选择性必修第四册"]


def std_ids(topic):
    return [s["id"].split(":", 1)[-1] for s in topic.get("standards", [])]


def main():
    topics = json.load(open(TOPICS, encoding="utf-8"))
    eng = [t for t in topics if t.get("subject") == "english"]
    units = [t for t in eng if t.get("level") == "unit"]
    papers = [t for t in eng if t.get("level") == "paper"]

    by_book = OrderedDict((b, []) for b in BOOK_ORDER)
    for t in units:
        by_book.setdefault(t["book"], []).append(t)
    paper_by_book = {p["book"]: p for p in papers}

    lines = []
    add = lines.append
    add("# 英语（三至十二年级，含高中）册次、Unit 与册末卷知识点清单")
    add("")
    add("> 由 `python3 scripts/gen_english_doc.py` 从 `data/topics.json` 自动生成；"
        "共 **%d 个知识点**（%d 个教材 Unit + %d 套册末卷）。" % (len(eng), len(units), len(papers)))
    add("> 教材：沪教版《英语》（上海教育出版社；义教段三年级起点，高中 2020 年经教育部审核通过）。"
        "义教段依据《义务教育英语课程标准（2022 年版）》，高中依据《普通高中英语课程标准（2017 年版 2020 年修订）》。")
    add("> 单元名称按公开电子课本与教辅目录整理，未逐页核对课本，教师使用前请以课本为准。")
    add("")
    add("所有英语知识点 id 以 `cne_` 开头，`subject: \"english\"`；Unit 级 `level: \"unit\"`、"
        "`chapter` 形如「三年级上 Unit 1 Hello!」；册末卷 `level: \"paper\"`、"
        "`chapter` 形如「三年级上 册末卷 期末模拟」。领域取 **语音 / 词汇 / 语法 / 日常表达 / 读写** 之一；"
        "与数学图不连边。")
    add("")
    add("先修边规则：同册「上一 Unit → 本 Unit」为 hard；「上一册末 Unit → 本册首 Unit」为 hard；"
        "每册每个领域第一个 Unit 与前面最近一个同领域 Unit 之间补一条 soft 边；"
        "册末卷只与本册首、末 Unit 各连一条 soft 边，不进入常规单点路径。")
    add("")
    add("| 册次 | Unit 数 | 册末卷 | 知识点 id 区间 |")
    add("|---|---:|---|---|")
    for book, ts in by_book.items():
        if not ts:
            continue
        paper = paper_by_book.get(book)
        add("| %s | %d | %s | `%s` – `%s` |" % (
            book, len(ts), ("`%s`" % paper["id"]) if paper else "—", ts[0]["id"], ts[-1]["id"]))
    add("| **合计** | **%d** | **%d** | |" % (len(units), len(papers)))
    add("")

    for book, ts in by_book.items():
        if not ts:
            continue
        add("## %s（%d 个 Unit）" % (book, len(ts)))
        add("")
        add("| # | 教材 Unit | 知识点 | 领域 | id | 课标 |")
        add("|---:|---|---|---|---|---|")
        for t in ts:
            unit = t["chapter"].split(" Unit ", 1)[1]
            add("| %s | %s | %s | %s | `%s` | %s |" % (
                unit.split(" ")[0], unit.split(" ", 1)[1] if " " in unit else unit,
                t["name"].split("（")[0], t["domain"], t["id"], "、".join(std_ids(t))))
        paper = paper_by_book.get(book)
        if paper:
            add("")
            add("**册末卷**：`%s` %s —— %s（10 题；课标：%s）" % (
                paper["id"], paper["chapter"], paper["name"], "、".join(std_ids(paper))))
        add("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print("已写入 %s（%d 个 Unit + %d 套册末卷）" % (OUT, len(units), len(papers)))


if __name__ == "__main__":
    main()
