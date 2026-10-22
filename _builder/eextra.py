# -*- coding: utf-8 -*-
"""把「每个 Unit 再加 2 类题」的扩充素材装配成题目。

三份素材（按学段分开维护）：
- ex_primary.EXTRA[(册, Unit 序号)] = {
      "p": 含 {1}…{5} 占位符的短文（首字母填空）,
      "a": [答案或 (答案, [可接受写法]), …],
      "s": (打乱顺序的词组, 正确句子, [可接受写法]) }
- ex_junior.EXTRA[(册, Unit 序号)] = {
      "p": 含 {1}…{6} 的语篇语法填空短文,
      "a": [(所给词, 正确答案) 或 (所给词, 正确答案, [可接受写法]), …],
      "q": (中文情景, 英文应答, [可接受写法]) }
- ex_high.EXTRA[(册, Unit 序号)] = {
      "p": 含 {1}…{10} 的语篇语法填空短文,
      "a": [(所给词, 正确答案), …],
      "t": [(中文句子, 英文译文, [可接受写法]), …] }

装配规则：短文的每个空各自成为一道 short 题（题干带完整短文与本题提示，
解析给出全篇答案），这样每个空都能被精确判分；打乱词组 / 情景问答 / 中译英
各是一道 short 题。
"""

try:
    import ex_high
except ImportError:          # 允许先写一部分数据
    ex_high = None
try:
    import ex_junior
except ImportError:
    ex_junior = None
try:
    import ex_primary
except ImportError:
    ex_primary = None


PRIMARY_COUNT = 5
JUNIOR_COUNT = 6
HIGH_COUNT = 10


def _sentence(text):
    """避免「。」与句末标点重复（如 Good afternoon, Kitty!。）。"""
    while len(text) > 1 and text.endswith("。") and text[-2] in ".!?。！？":
        text = text[:-1]
    return text


def _as_list(value):
    if not value:
        return []
    if isinstance(value, str):
        return [value]
    return list(value)


def _answer_of(item, style):
    """返回 (答案, 可接受写法)。

    style="primary"：["答案", ("答案", [可接受写法])]，空格答案本身即答案；
    style="given"：[(所给词, 答案[, 可接受写法])]，第二个元素才是答案。
    """
    if style == "primary":
        if isinstance(item, str):
            return item, []
        if len(item) == 2:
            return item[0], _as_list(item[1])
        return item[0], _as_list(item[2])
    if isinstance(item, str):
        return item, []
    if len(item) == 2:
        return item[1], []
    return item[1], _as_list(item[2])


def _blank_difficulty(index, total):
    if index <= 2:
        return "basic"
    if index <= total * 0.7:
        return "standard"
    return "advanced"


def _blanks(passage, answers, hint_of, label, style="primary"):
    """把一篇多空短文拆成逐空的 short 题。"""
    key = "、".join(_answer_of(a, style)[0] for a in answers)
    out = []
    total = len(answers)
    for i, item in enumerate(answers, 1):
        ans, accept = _answer_of(item, style)
        hint = hint_of(item, ans, i)
        if style == "given" and isinstance(item, tuple) and item[0].strip().lower() == ans.strip().lower():
            hint += "（本空照填原词，不需变形）"
        out.append({
            "difficulty": _blank_difficulty(i, total),
            "type": "short",
            "prompt": "%s（第 %d 空）。\n%s\n提示：%s" % (label, i, passage, hint),
            "answer": ans,
            "exact": True,
            "explanation": _sentence("第 %d 空填 %s。本篇答案：%s。" % (i, ans, key)),
            **({"accept": accept} if accept else {}),
        })
    return out


def primary_questions(vol, no):
    data = (getattr(ex_primary, "EXTRA", {}) or {}).get((vol, no))
    if not data:
        return []
    qs = _blanks(data["p"], data["a"],
                 lambda item, ans, i: "首字母 %s" % ans[0], "根据首字母补全短文",
                 style="primary")
    scramble = data.get("s")
    if scramble:
        words, answer = scramble[0], scramble[1]
        accept = list(scramble[2]) if len(scramble) > 2 else []
        qs.append({
            "difficulty": "basic",
            "type": "short",
            "prompt": "连词成句（注意大小写与句末标点）：%s" % words,
            "answer": answer,
            "explanation": _sentence("正确句子：%s。" % answer),
            **({"accept": accept} if accept else {}),
        })
    return qs


def junior_questions(vol, no):
    data = (getattr(ex_junior, "EXTRA", {}) or {}).get((vol, no))
    if not data:
        return []
    qs = _blanks(data["p"], data["a"],
                 lambda item, ans, i: "所给词 %s" % item[0], "用括号内所给词的正确形式填空",
                 style="given")
    qa = data.get("q")
    if qa:
        question, answer = qa[0], qa[1]
        accept = list(qa[2]) if len(qa) > 2 else []
        qs.append({
            "difficulty": "standard",
            "type": "short",
            "prompt": question,
            "answer": answer,
            "explanation": _sentence("参考答案：%s。" % answer),
            **({"accept": accept} if accept else {}),
        })
    return qs


def high_questions(vol, no):
    data = (getattr(ex_high, "EXTRA", {}) or {}).get((vol, no))
    if not data:
        return []
    qs = _blanks(data["p"], data["a"],
                 lambda item, ans, i: "所给词 %s" % item[0],
                 "语篇语法填空（用所给词的正确形式或适当的词填空）", style="given")
    diffs = ["basic", "standard", "advanced"]
    for i, item in enumerate(data.get("t") or []):
        zh, en = item[0], item[1]
        accept = list(item[2]) if len(item) > 2 else []
        qs.append({
            "difficulty": diffs[min(i, 2)],
            "type": "short",
            "prompt": "中译英：%s" % zh,
            "answer": en,
            "explanation": _sentence("参考译文：%s。" % en),
            **({"accept": accept} if accept else {}),
        })
    return qs
