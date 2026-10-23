# -*- coding: utf-8 -*-
"""沪教版高中数学（2020 年审定）知识点的通用构造器。

- 册次与年级：必修第一册=10 上、必修第二册=10 下、必修第三册=11 上、
  选择性必修第一册=11 下、选择性必修第二册=12 上、选择性必修第三册=12 下。
- chapter 形如「必修第一册 第1章 集合与逻辑 1.1 集合及其表示法」，卷名取教材册名。
- id 前缀 cnm_，与小学、初中连续编号；课标前缀 cmh-2017:（高中数学课标）。
- 题目以 numeric / choice 为主，尽量给出可复算的 verify 表达式。
"""

VOLUMES = {
    "必修第一册": (10, "上"),
    "必修第二册": (10, "下"),
    "必修第三册": (11, "上"),
    "选择性必修第一册": (11, "下"),
    "选择性必修第二册": (12, "上"),
    "选择性必修第三册": (12, "下"),
}


def qn(diff, prompt, answer, explanation, verify=None):
    """数值题。verify 是可用 scripts/verify_questions.py 独立复算的表达式。"""
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


def topic(num, volume, chapter_no, chapter_name, section, name, domain, ttype,
          desc, mastery, ex, mistakes, tip, prereqs, stds, qs, key_points=None):
    """构造一个高中数学知识点。

    num        编号（写入 cnm_<三位数>）
    volume     "高一上" 等，决定 grade / semester
    chapter_no "第1章"，chapter_name "集合与逻辑"，section "1.1 集合初步"
    prereqs    先修列表，元素为 "cnm_xxx" 或 ("cnm_xxx", "soft")，缺省 hard
    stds       "1.NA.01,1.NA.02" 这样的课标编号（不加前缀）
    """
    assert volume in VOLUMES, volume
    assert domain in ("数与代数", "图形与几何", "统计与概率", "综合与实践"), domain
    assert ttype in ("conceptual", "procedural", "reasoning", "application", "modeling")
    grade, semester = VOLUMES[volume]
    tid = "cnm_%03d" % num
    chapter = "%s %s %s" % (volume, chapter_no, chapter_name)
    if section:
        chapter += " " + section

    pre = []
    for p in prereqs:
        if isinstance(p, str):
            pre.append((p, "hard"))
        else:
            pre.append((p[0], p[1] if len(p) > 1 else "hard"))

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
    diag_answer = (next(t for k, t in first["choices"] if k == first["answer"])
                   if first["type"] == "choice" else str(first["answer"]))

    standards = []
    for sid in [s.strip() for s in stds.split(",") if s.strip()]:
        if not sid.startswith("cmh-2017:"):
            sid = "cmh-2017:" + sid
        standards.append({"id": sid, "confidence": "exact"})

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
