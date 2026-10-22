# -*- coding: utf-8 -*-
"""沪教版英语（小学三至五年级、初中六至九年级）知识点构造器。

与数学共用同一套数据结构，只额外加 `subject: "english"`，
并使用 cne_ 前缀的 id 与 语音/词汇/语法/日常表达/读写 五个领域。
"""

DOMAINS = ["语音", "词汇", "语法", "日常表达", "读写"]

VOLUMES = {
    "3上": (3, "上"), "3下": (3, "下"),
    "4上": (4, "上"), "4下": (4, "下"),
    "5上": (5, "上"), "5下": (5, "下"),
    "6上": (6, "上"), "6下": (6, "下"),
    "7上": (7, "上"), "7下": (7, "下"),
    "8上": (8, "上"), "8下": (8, "下"),
    "9上": (9, "上"), "9下": (9, "下"),
}
VOLUME_ZH = {"3上": "三年级上", "3下": "三年级下",
             "4上": "四年级上", "4下": "四年级下",
             "5上": "五年级上", "5下": "五年级下",
             "6上": "六年级上", "6下": "六年级下", "7上": "七年级上", "7下": "七年级下",
             "8上": "八年级上", "8下": "八年级下", "9上": "九年级上", "9下": "九年级下"}


def eq(diff, prompt, choices, answer, explanation):
    """英语选择题。choices 为 [(key, text)]。"""
    assert answer in [k for k, _ in choices], (prompt, answer)
    return {
        "difficulty": diff,
        "type": "choice",
        "prompt": prompt,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
    }


def es(diff, prompt, answer, explanation, accept=None):
    """英语短答题（拼写、填空、词形变化）。答案按规范化后精确匹配，accept 放宽可接受写法。"""
    return {
        "difficulty": diff,
        "type": "short",
        "prompt": prompt,
        "answer": answer,
        "explanation": explanation,
        **({"accept": accept} if accept else {}),
    }


def etopic(num, vol, chapter_tail, name, domain, ttype, desc, mastery, ex, mistakes, tip,
           prereqs, stds, qs, note=None, root_reason=None):
    """构造一个英语知识点。

    num          编号（写入 cne_<三位数>）
    vol          "6上" 等，用于生成册次与章节
    chapter_tail 章节尾部，如 "全册 核心语法：一般现在时"
    stds         "2.GR.01" 或 "2.GR.01,2.VO.02"（自动补 ces-2022: 前缀）
    ex           (题干, [步骤...], 答案)
    """
    assert domain in DOMAINS, domain
    tid = "cne_%03d" % num
    grade, semester = VOLUMES[vol]
    chapter = "%s %s" % (VOLUME_ZH[vol], chapter_tail)

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
        if q.get("accept"):
            qd["accept"] = [str(x) for x in q["accept"]]
        questions.append(qd)

    # 题库约定：除 q1 外还要有一道 basic
    qs = [dict(q) for q in qs]
    first = qs[0]
    if first["type"] == "choice":
        diag_answer = next(t for k, t in first["choices"] if k == first["answer"])
    else:
        diag_answer = str(first["answer"])

    standards = []
    for sid in [s.strip() for s in stds.split(",") if s.strip()]:
        item = {"id": "ces-2022:" + sid, "confidence": "exact"}
        if note:
            item["note"] = note
        standards.append(item)

    topic = {
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
        "subject": "english",
        "standards": standards,
        "tutoring": {
            "key_points": list(mastery),
            "worked_example": {"problem": ex[0], "steps": list(ex[1]), "answer": str(ex[2])},
            "common_mistakes": list(mistakes),
            "coaching_tip": tip,
        },
    }
    if root_reason:
        topic["root_reason"] = root_reason
    pre = [(p, "hard") if isinstance(p, str) else (p[0], p[1] if len(p) > 1 else "hard") for p in prereqs]
    return {"topic": topic, "prereqs": pre, "questions": questions}
