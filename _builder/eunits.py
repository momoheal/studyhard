# -*- coding: utf-8 -*-
"""把 Unit 目录装配成知识点 / 先修边 / 题目。

输入：
- eu_primary.UNITS：小学三至六年级，每册 12 个 Unit；
- eu_junior.UNITS ：初中七至九年级，每册 6—8 个 Unit；
- eu_high.UNITS   ：高中必修与选择性必修，每册 4 个 Unit。

输出与 ecommon.eunit() 一致：每册内按「上一 Unit → 本 Unit」串成 hard 边，
册与册之间用「上一册末 Unit → 本册首 Unit」连接；另外为每册每个领域的第一个 Unit
补一条跨册同领域的 soft 边。id 按册次与 Unit 顺序编号为 cne_001、cne_002 ……
"""

import estandards
from ecommon import VOLUMES, VOLUME_ZH, eunit

import eu_high
import eu_junior
import eu_primary

ELEMENTARY_VOLUMES = ["3上", "3下", "4上", "4下", "5上", "5下", "6上", "6下"]
JUNIOR_VOLUMES = ["7上", "7下", "8上", "8下", "9上", "9下"]

DOMAIN_CODE = {"语音": "PH", "词汇": "VO", "语法": "GR", "日常表达": "PU", "读写": "DS"}
DOMAIN_TYPE = {"语音": "conceptual", "词汇": "conceptual", "语法": "procedural",
               "日常表达": "application", "读写": "application"}
DOMAIN_MASTERY = {
    "语音": "能读准本单元的语音要点，并在朗读或对话中体现出来。",
    "词汇": "能根据中文提示写出本单元核心词，并在句中正确使用。",
    "语法": "能识别本单元语法点在句中的形式，并正确完成填空。",
    "日常表达": "能在本单元情境中完成问答、请求与翻译。",
    "读写": "能读懂并把本单元话题的句子译成英文。",
}
DOMAIN_MISTAKE = {
    "语音": "朗读时忽略单词重音与句子的语调。",
    "词汇": "可数名词单复数与冠词漏用（如 a apple、two cat）。",
    "语法": "忽略时态与人称，谓语形式用错。",
    "日常表达": "问答时漏掉助动词或答语与问句不匹配。",
    "读写": "句首字母未大写、句末缺标点，或时态前后不一致。",
}

STANDARDS_BY_STAGE_DOMAIN = {}
for _sid, _stage, _dom, _theme, _text in estandards.ITEMS:
    STANDARDS_BY_STAGE_DOMAIN.setdefault((_stage, _dom), []).append(_sid)

# 课标条目按「语音／词汇／语法／语篇／语用」分域，书中的「日常表达」「读写」分别对应「语用」「语篇」
DOMAIN_CODE_DOMAIN = {"语音": "语音", "词汇": "词汇", "语法": "语法",
                      "日常表达": "语用", "读写": "语篇"}

STAGE_OF_GRADE = {3: "一级", 4: "一级", 5: "二级", 6: "二级", 7: "三级", 8: "三级", 9: "三级"}

ROOT_REASON = ("沪教版英语从三年级起开设（三年级起点），本知识点是全图英语部分的起点，"
               "前面没有更早的英语知识点。")


def _assign_standards(meta):
    """按「学段 × 领域」分组分配课标条目，保证该组下每条课标都至少被引用一次。

    meta 为 [(stage, domain), ...]，与知识点顺序一致；返回 [["1.VO.01", ...], ...]。
    每条知识点最多 3 条：先平分本领域条目，不足 2 条时补一条「语篇／语用」条目。
    """
    groups = {}
    for i, (stage, dom) in enumerate(meta):
        groups.setdefault((stage, dom), []).append(i)

    out = [[] for _ in meta]
    for (stage, dom), idxs in groups.items():
        items = STANDARDS_BY_STAGE_DOMAIN[(stage, DOMAIN_CODE_DOMAIN.get(dom, dom))]
        for j, i in enumerate(idxs):
            out[i].append((items[j % len(items)], "exact"))

    counters = {}
    for i, (stage, dom) in enumerate(meta):
        if len(out[i]) >= 3:
            continue
        if len(out[i]) < 2:
            sec_dom = "语篇" if dom != "读写" else "语用"
            pool = STANDARDS_BY_STAGE_DOMAIN[(stage, sec_dom)]
            k = counters.get((stage, sec_dom), 0)
            counters[(stage, sec_dom)] = k + 1
            item = pool[k % len(pool)]
            if item not in [x for x, _ in out[i]]:
                out[i].append((item, "inferred"))

    # 兜底：学段内仍有课标条目没被任何知识点引用时，补到该学段课标条数最少的 Unit（每点最多 3 条）。
    # 这些条目（多为语音／词汇类通识要求）在每个 Unit 的朗读与词汇教学中都会涉及。
    covered = {x for lst in out for x, _ in lst}
    for stage in sorted({m[0] for m in meta if m[0]}):
        missing = [x for dom in ("语音", "词汇", "语法", "语篇", "语用")
                   for x in STANDARDS_BY_STAGE_DOMAIN.get((stage, dom), []) if x not in covered]
        if not missing:
            continue
        idxs = sorted([i for i, m in enumerate(meta) if m[0] == stage], key=lambda i: len(out[i]))
        for item in missing:
            for i in idxs:
                if len(out[i]) < 3 and item not in [x for x, _ in out[i]]:
                    out[i].append((item, "inferred"))
                    covered.add(item)
                    break
    return out


def _rotate(items, shift):
    shift %= len(items)
    return items[shift:] + items[:shift]


def _key_of(text, order):
    return "ABCD"[order.index(text)]


def _primary_questions(rec):
    """由 (words, blank, trans) 生成 4 道题：2 选择 + 2 短答，覆盖 basic 与 standard。"""
    vol, no, unit, theme, dom, words, blank, trans = rec
    ens = [w[0] for w in words]
    idx = (no - 1) % len(ens)

    target = words[idx]
    distractors = [w for w in words if w[0] != target[0]][:2]
    options = _rotate([target[0]] + [d[0] for d in distractors], (no + len(unit)) % 3)
    q1 = ("choice", "basic", "「%s」的英文是（　）。" % target[1],
          [(k, o) for k, o in zip("ABC", options)], "ABC"[options.index(target[0])],
          "%s 意为“%s”；其余选项分别是 %s。" % (
              target[0], target[1], "、".join("“%s”" % d[1] for d in distractors)))

    spell = words[(idx + 1) % len(words)]
    q2 = ("short", "basic", "根据中文写出英文单词：%s ______" % spell[1],
          spell[0], "「%s」的英文是 %s。" % (spell[1], spell[0]),
          [spell[0], spell[0][:1].upper() + spell[0][1:]])

    sent, ans, expl = blank
    fill_distractors = [e for e in ens if e.lower() != ans.lower()][:2]
    opts3 = _rotate([ans] + fill_distractors, no % 3)
    # 空格答案是本单元核心词时给出中文提示，避免同单元近义词也能填入造成多解
    hint = next((z for e, z in words if e.lower() == ans.lower()), None)
    prompt3 = "选词填空（提示：%s）：%s" % (hint, sent) if hint else "选词填空：%s" % sent
    q3 = ("choice", "standard", prompt3,
          [(k, o) for k, o in zip("ABC", opts3)], "ABC"[opts3.index(ans)], expl)

    zh, en, accept = trans
    q4 = ("short", "standard", "翻译：%s" % zh, en, "参考译文：%s" % en, accept)
    return [q1, q2, q3, q4]


def _questions_from_tuples(rows):
    """rows 元素为 (kind, difficulty, prompt, answer|options, explanation, accept)。"""
    qs = []
    for kind, diff, prompt, ans, expl, extra in rows:
        if kind == "choice":
            qs.append({"difficulty": diff, "type": "choice", "prompt": prompt,
                       "choices": [(k, t) for k, t in ans], "answer": expl, "explanation": extra})
        else:
            q = {"difficulty": diff, "type": "short", "prompt": prompt,
                 "answer": ans, "explanation": expl}
            if extra:
                q["accept"] = list(extra)
            qs.append(q)
    return qs


def _pack(rec, num, prereqs, stds, root=False):
    vol, no, unit, theme, dom, words, blank, trans = rec
    book = VOLUME_ZH[vol]
    grade = VOLUMES[vol][0]
    word_list = "、".join("%s（%s）" % (e, z) for e, z in words)
    desc = ("本知识点对应沪教版《英语》%s Unit %d %s，主题为%s。"
            "本单元核心词：%s。" % (book, no, unit, theme, word_list))
    mastery = [
        "能认读并运用本单元核心词：%s。" % "、".join(e for e, _ in words),
        DOMAIN_MASTERY[dom],
    ]
    mistakes = [
        "核心词拼写不准确，如 %s 漏写或写错字母。" % words[0][0],
        DOMAIN_MISTAKE[dom],
    ]
    expl = blank[2]
    ex = (blank[0], ["先判断空格在句中的成分与语境。", expl, "因此填 %s。" % blank[1]], blank[1])
    tip = "先跟读本单元对话，再用 %s 造两个句子，最后完成 4 道练习。" % words[0][0]

    rows = _primary_questions(rec)
    return eunit(num, vol, no, unit, theme, dom, DOMAIN_TYPE[dom], desc, mastery, ex,
                 mistakes, tip, prereqs, stds, _questions_from_tuples(rows),
                 std_prefix="ces-2022:",
                 root_reason=ROOT_REASON if root else None)


def _pack_high(rec, num, prereqs, root=False):
    vol, no, unit, theme, dom = rec["vol"], rec["no"], rec["unit"], rec["theme"], rec["dom"]
    book = VOLUME_ZH[vol]
    desc = rec["desc"]
    ex = rec["ex"]
    return eunit(num, vol, no, unit, theme, dom, DOMAIN_TYPE[dom], desc, rec["mastery"], ex,
                 rec["mistakes"], rec["tip"], prereqs, rec["stds"], list(rec["qs"]),
                 std_prefix="chs-2017:",
                 root_reason=ROOT_REASON if root else None)


def build():
    """返回 (packs, volumes)。volumes 为按册次排列的 [(册, 起止编号)]，供统计用。"""
    packs = []
    order = [(vol, None) for vol in
             ELEMENTARY_VOLUMES + JUNIOR_VOLUMES +
             ["必修一", "必修二", "必修三", "选必一", "选必二", "选必三", "选必四"]]

    records = []
    for vol in ELEMENTARY_VOLUMES:
        records += [(vol, rec) for rec in eu_primary.UNITS if rec[0] == vol]
    for vol in JUNIOR_VOLUMES:
        records += [(vol, rec) for rec in eu_junior.UNITS if rec[0] == vol]
    for vol in ["必修一", "必修二", "必修三", "选必一", "选必二", "选必三", "选必四"]:
        records += [(vol, rec) for rec in eu_high.UNITS if rec["vol"] == vol]

    ids_by_vol = {}
    for i, (vol, rec) in enumerate(records, 1):
        ids_by_vol.setdefault(vol, []).append("cne_%03d" % i)

    meta = []
    for vol, rec in records:
        if isinstance(rec, tuple):
            grade = VOLUMES[vol][0]
            meta.append((STAGE_OF_GRADE[grade], rec[4]))
        else:
            meta.append((None, rec["dom"]))
    auto_stds = _assign_standards([m for m in meta if m[0] is not None])

    last_domain_unit = {}      # domain -> 最近的 Unit id
    prev_vol_last = None
    for i, (vol, rec) in enumerate(records, 1):
        tid = "cne_%03d" % i
        no = rec[1] if isinstance(rec, tuple) else rec["no"]
        dom = rec[4] if isinstance(rec, tuple) else rec["dom"]
        prereqs = []
        if i == 1:
            root = True
        else:
            root = False
            prereqs.append(prev_vol_last)          # 跨册衔接
        # 同册上一 Unit
        units_in_vol = ids_by_vol[vol]
        j = units_in_vol.index(tid)
        if j > 0:
            prereqs = [units_in_vol[j - 1]] + [p for p in prereqs if p != units_in_vol[j - 1]]
        # 跨册同领域 soft 边
        soft = last_domain_unit.get(dom)
        if soft and soft not in prereqs:
            prereqs.append((soft, "soft"))
        last_domain_unit[dom] = tid
        prev_vol_last = tid

        if isinstance(rec, tuple):
            pack = _pack(rec, i, prereqs, auto_stds.pop(0), root)
        else:
            pack = _pack_high(rec, i, prereqs, root)
        packs.append(pack)

    return packs, order
