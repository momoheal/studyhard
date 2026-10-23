# -*- coding: utf-8 -*-
"""沪教版英语知识点构造器（小学一至九年级 + 高中必修/选择性必修）。

与数学共用同一套数据结构，只额外加 `subject: "english"`，
并使用 cne_ 前缀的 id 与 语音/词汇/语法/日常表达/读写 五个领域。

两套构造器：
- `etopic()`：册 × 领域 的模块级知识点（第一阶段的写法，保留兼容）；
- `eunit()` ：教材 Unit 级知识点，chapter 形如「三年级上 Unit 1 Hello!」，
  高中为「必修第一册 Unit 1 Our world」，grade 10/11/12 分别为高一/高二/高三。
"""

DOMAINS = ["语音", "词汇", "语法", "日常表达", "读写"]

VOLUMES = {
    "1上": (1, "上"), "1下": (1, "下"),
    "2上": (2, "上"), "2下": (2, "下"),
    "3上": (3, "上"), "3下": (3, "下"),
    "4上": (4, "上"), "4下": (4, "下"),
    "5上": (5, "上"), "5下": (5, "下"),
    "6上": (6, "上"), "6下": (6, "下"),
    "7上": (7, "上"), "7下": (7, "下"),
    "8上": (8, "上"), "8下": (8, "下"),
    "9上": (9, "上"), "9下": (9, "下"),
    # 高中（沪教版 2020 年审定）：每册 4 个 Unit
    "必修一": (10, "上"), "必修二": (10, "下"), "必修三": (11, "上"),
    "选必一": (11, "下"), "选必二": (12, "上"),
    "选必三": (12, "下"), "选必四": (12, "下"),
}
VOLUME_ZH = {"1上": "一年级上", "1下": "一年级下",
             "2上": "二年级上", "2下": "二年级下",
             "3上": "三年级上", "3下": "三年级下",
             "4上": "四年级上", "4下": "四年级下",
             "5上": "五年级上", "5下": "五年级下",
             "6上": "六年级上", "6下": "六年级下",
             "7上": "七年级上", "7下": "七年级下",
             "8上": "八年级上", "8下": "八年级下",
             "9上": "九年级上", "9下": "九年级下",
             "必修一": "必修第一册", "必修二": "必修第二册", "必修三": "必修第三册",
             "选必一": "选择性必修第一册", "选必二": "选择性必修第二册",
             "选必三": "选择性必修第三册", "选必四": "选择性必修第四册"}


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


def _format_questions(tid, qs):
    """把 eq()/es() 生成的题目转成 data/questions.json 的结构，并给出 q1 的判分答案。"""
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
        if q.get("exact"):
            qd["exact"] = True
        questions.append(qd)
    first = qs[0]
    if first["type"] == "choice":
        diag_answer = next(t for k, t in first["choices"] if k == first["answer"])
    else:
        diag_answer = str(first["answer"])
    return questions, diag_answer


def _format_standards(stds, prefix, note=None):
    """stds 可以是 "1.VO.01,1.PH.02" 字符串（全部 exact），也可以是 [(id, confidence), ...]。"""
    if isinstance(stds, str):
        pairs = [(s.strip(), "exact") for s in stds.split(",") if s.strip()]
    else:
        pairs = [(s, c) for s, c in stds]
    out = []
    for sid, conf in pairs:
        item = {"id": prefix + sid, "confidence": conf}
        if note:
            item["note"] = note
        out.append(item)
    return out


def _format_prereqs(prereqs):
    return [(p, "hard") if isinstance(p, str) else (p[0], p[1] if len(p) > 1 else "hard")
            for p in prereqs]


def eunit(num, vol, unit_no, unit_name, theme, domain, ttype, desc, mastery, ex, mistakes, tip,
          prereqs, stds, qs, std_prefix="ces-2022:", note=None, root_reason=None):
    """构造一个 Unit 级英语知识点。

    num        编号（写入 cne_<三位数>）
    vol        "3上" / "必修一" 等，决定 grade、semester 与册名
    unit_no    教材中的 Unit 序号
    unit_name  教材中的 Unit 名称，如 "Hello!"
    theme      中文主题，用于 name（"问候与自我介绍（Unit 1 Hello!）"）
    chapter    自动拼成「三年级上 Unit 1 Hello!」
    """
    assert domain in DOMAINS, domain
    tid = "cne_%03d" % num
    grade, semester = VOLUMES[vol]
    book = VOLUME_ZH[vol]
    questions, diag_answer = _format_questions(tid, qs)

    topic = {
        "id": tid,
        "name": "%s（Unit %d %s）" % (theme, unit_no, unit_name),
        "domain": domain,
        "grade": grade,
        "semester": semester,
        "chapter": "%s Unit %d %s" % (book, unit_no, unit_name),
        "type": ttype,
        "description": desc,
        "mastery_criteria": list(mastery),
        "diagnostic_question": {"question": questions[0]["prompt"], "answer": diag_answer},
        "external": False,
        "subject": "english",
        "level": "unit",
        "book": book,
        "unit_no": unit_no,
        "standards": _format_standards(stds, std_prefix, note),
        "tutoring": {
            "key_points": list(mastery),
            "worked_example": {"problem": ex[0], "steps": list(ex[1]), "answer": str(ex[2])},
            "common_mistakes": list(mistakes),
            "coaching_tip": tip,
        },
    }
    if root_reason:
        topic["root_reason"] = root_reason
    return {"topic": topic, "prereqs": _format_prereqs(prereqs), "questions": questions}


def etopic(num, vol, chapter_tail, name, domain, ttype, desc, mastery, ex, mistakes, tip,
           prereqs, stds, qs, note=None, root_reason=None):
    """构造一个模块级（册 × 领域）英语知识点。"""
    assert domain in DOMAINS, domain
    tid = "cne_%03d" % num
    grade, semester = VOLUMES[vol]
    chapter = "%s %s" % (VOLUME_ZH[vol], chapter_tail)
    questions, diag_answer = _format_questions(tid, qs)

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
        "diagnostic_question": {"question": questions[0]["prompt"], "answer": diag_answer},
        "external": False,
        "subject": "english",
        "level": "module",
        "standards": _format_standards(stds, "ces-2022:", note),
        "tutoring": {
            "key_points": list(mastery),
            "worked_example": {"problem": ex[0], "steps": list(ex[1]), "answer": str(ex[2])},
            "common_mistakes": list(mistakes),
            "coaching_tip": tip,
        },
    }
    if root_reason:
        topic["root_reason"] = root_reason
    return {"topic": topic, "prereqs": _format_prereqs(prereqs), "questions": questions}

def epaper(num, vol, title, desc, mastery, tip, qs, prereqs, stds, mistakes, ex,
           std_prefix="ces-2022:", root_reason=None):
    """构造一个「册末卷」知识点（level: "paper"）。

    chapter 形如「三年级上 册末卷 期末模拟」，grade/semester 与所在册一致；
    qs 为 eq()/es()/eself() 生成的题目列表（整卷题目都在这个知识点上）。
    """
    tid = "cne_%03d" % num
    grade, semester = VOLUMES[vol]
    book = VOLUME_ZH[vol]
    questions, diag_answer = _format_questions(tid, qs)
    topic = {
        "id": tid,
        "name": "%s（%s册末卷）" % (title, book),
        "domain": "读写",
        "grade": grade,
        "semester": semester,
        "chapter": "%s 册末卷 %s" % (book, title),
        "type": "application",
        "description": desc,
        "mastery_criteria": list(mastery),
        "diagnostic_question": {"question": questions[0]["prompt"], "answer": diag_answer},
        "external": False,
        "subject": "english",
        "level": "paper",
        "book": book,
        "standards": _format_standards(stds, std_prefix),
        "tutoring": {
            "key_points": list(mastery),
            "worked_example": {"problem": ex[0], "steps": list(ex[1]), "answer": str(ex[2])},
            "common_mistakes": list(mistakes),
            "coaching_tip": tip,
        },
    }
    if root_reason:
        topic["root_reason"] = root_reason
    return {"topic": topic, "prereqs": _format_prereqs(prereqs), "questions": questions}
