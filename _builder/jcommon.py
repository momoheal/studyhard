# -*- coding: utf-8 -*-
"""沪教版初中（六至九年级·五四学制）知识点的通用构造器。

设计目标：
- 让每个内容模块只写“真正需要人写的部分”：章节、名称、描述、掌握标准、
  例题、易错点、辅导提示、先修、课标映射、题目。
- 统一生成 topics / dependencies / questions 三份数据的字段结构，
  与小学段（_builder/common.py 生成、data/*.json 保存）完全一致。
- 诊断题直接取第 1 题，避免“诊断题与题库不一致”。
"""


def qn(diff, prompt, answer, explanation, verify=None):
    """数值题。verify 是可用脚本独立复算的表达式（尽量都写）。"""
    d = {
        "difficulty": diff,
        "type": "numeric",
        "prompt": prompt,
        "answer": str(answer),
        "explanation": explanation,
    }
    if verify:
        d["verify"] = verify
    return d


def qc(diff, prompt, choices, answer, explanation):
    """选择题。choices 形如 [("A", "……"), ("B", "……"), ("C", "……")]。"""
    return {
        "difficulty": diff,
        "type": "choice",
        "prompt": prompt,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
    }


def topic(num, chapter, name, domain, ttype, desc, mastery, ex, mistakes, tip,
          prereqs, stds, qs, key_points=None):
    """构造一个正式知识点。

    num      知识点编号（写入 cnm_<三位数>）
    chapter  完整章节串，如 "六年级上 第一章 数的整除 1.1 整数和整除的意义"
             首段必须是册次（六年级上/六年级下/……），供前端与诊断工具解析。
    ex       (题面, [步骤...], 答案) 课本同步精讲例题
    prereqs  先修列表，元素为 "cnm_xxx" 或 ("cnm_xxx", "soft")，缺省 hard
    stds     课标条目，如 "4.NA.01" 或 "4.NA.01,4.NA.07"
    """
    tid = "cnm_%03d" % num
    pre = []
    for p in prereqs:
        if isinstance(p, str):
            pre.append((p, "hard"))
        else:
            pre.append((p[0], p[1] if len(p) > 1 else "hard"))

    # 题库约定（见 tests/test_engine.js）：每个知识点除 q1 外至少还要有一道 basic 题。
    # 若作者只写了 q1 一道 basic，就把后面第一道 standard 题降为 basic
    # （这些题通常是单一事实判断，标 basic 也符合实际难度）。
    qs = [dict(q) for q in qs]
    if not any(q["difficulty"] == "basic" for q in qs[1:]):
        for q in qs[1:]:
            if q["difficulty"] == "standard":
                q["difficulty"] = "basic"
                break

    questions = []
    for i, q in enumerate(qs, 1):
        qd = {
            "id": "%s_q%d" % (tid, i),
            "topicId": tid,
            "difficulty": q["difficulty"],
            "type": q["type"],
            "prompt": q["prompt"],
            "answer": str(q["answer"]),
            "explanation": q["explanation"],
        }
        if q["type"] == "choice":
            qd["choices"] = [{"key": k, "text": t} for k, t in q["choices"]]
        if q.get("verify"):
            qd["verify"] = q["verify"]
        if q.get("unordered"):
            qd["unordered"] = True
        questions.append(qd)

    first = qs[0]
    if first["type"] == "choice":
        diag_answer = next(t for k, t in first["choices"] if k == first["answer"])
    else:
        diag_answer = str(first["answer"])

    standards = []
    for sid in [s.strip() for s in stds.split(",") if s.strip()]:
        if not sid.startswith("cms-2022:"):
            sid = "cms-2022:" + sid
        standards.append({"id": sid, "confidence": "exact"})

    volume, _, _rest = chapter.partition(" ")
    grade = {"六": 6, "七": 7, "八": 8, "九": 9}[volume[0]]
    semester = volume[-1]
    assert semester in ("上", "下"), "章节串必须以“六年级上”这样的册次开头：%r" % chapter

    t = {
        "id": tid,
        "name": name,
        "domain": domain,
        "grade": grade,
        "semester": semester,
        "chapter": chapter,
        "type": ttype,
        "description": desc,
        "mastery_criteria": list(mastery),
        "diagnostic_question": {"question": first["prompt"], "answer": diag_answer},
        "external": False,
        "standards": standards,
        "tutoring": {
            "key_points": list(key_points or mastery),
            "worked_example": {
                "problem": ex[0],
                "steps": list(ex[1]),
                "answer": str(ex[2]),
            },
            "common_mistakes": list(mistakes),
            "coaching_tip": tip,
        },
    }
    return {"topic": t, "prereqs": pre, "questions": questions}
