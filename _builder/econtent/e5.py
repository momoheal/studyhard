# -*- coding: utf-8 -*-
"""沪教版英语 五年级上、下册（小学三起点；依据 2022 年版课标二级要求编写）。

五上 Module 1—4（12 个单元，话题为：认识新朋友、伙伴与家庭生活、外出活动、自然世界——
风、水、火等），五下 Module 1—4（话题为：五种感官的运用、身边的规则与变化、外出旅行、
自然与环保）。
"""

from ecommon import eq, es, etopic

TOPICS = [

    # ================================================================ 五年级上
    etopic(59, "5上", "全册 语音：句子重音与升降调", "句子重音与升降调", "语音", "procedural",
           "五上 Module 1—4 的对话与短文开始成段，朗读时句子的重音与升降调直接影响意思表达，"
           "如一般疑问句用升调、特殊疑问句用降调。",
           ["能重读句中的关键词（名词、动词、形容词）", "能用升调读一般疑问句、用降调读陈述句与特殊疑问句"],
           ("判断：句子 Where are you going? 朗读时句末用什么语调？",
            ["这是特殊疑问句", "特殊疑问句句末用降调", "所以用降调"],
            "降调。"),
           ["所有问句都用升调", "句中每个词都重读"],
           "把关键词用铅笔圈出来再读，读时圈出的词加重。",
           ["cne_054"], "1.PH.02,2.PH.03",
           [eq("basic", "朗读 Where are you going? 时，句末通常用（　）。",
               [("A", "升调"), ("B", "降调"), ("C", "平调")], "B",
               "特殊疑问句用降调。"),
            es("basic", "朗读一般疑问句 Are you ready? 时，句末通常用升调还是降调？填“升调”或“降调”。", "升调",
               "一般疑问句用升调。", accept=["升调"]),
            eq("standard", "句子 I like apples very much. 中，通常重读的词是（　）。",
               [("A", "I 和 very"), ("B", "like 和 apples"), ("C", "the 和 and")], "B",
               "实词 like、apples 重读；虚词弱读。"),
            es("advanced", "补全句子（注意大小写）：______ do you go to school? — By bus.", "How",
               "询问方式用 How，句首大写。", accept=["how", "How"])]),

    etopic(60, "5上", "全册 词汇：未来、出行与自然", "主题词汇与短语（未来·出行·自然）", "词汇", "conceptual",
           "五上 Module 1—4 的话题词：future、pilot、doctor、cook、birthday、party、bus、"
           "underground、beach、wind、water、fire、safe、dangerous 等。",
           ["能认读并拼写本册核心词", "能围绕职业与出行话题组句，注意介词搭配"],
           ("用英语说“我长大后想当一名飞行员。”",
            ["“想当”用 want to be", "将来用 will 或 want to be", "所以是 I want to be a pilot when I grow up."],
            "I want to be a pilot when I grow up."),
           ["职业名词前漏冠词（want to be pilot）", "by bus 写成 by the bus"],
           "职业词配一句职业描述：A pilot flies a plane. A cook makes food. 一行一组。",
           ["cne_055"], "1.VO.01,1.VO.02",
           [eq("basic", "My father is a ______ . He flies a plane.",
               [("A", "pilot"), ("B", "cook"), ("C", "driver")], "A",
               "开飞机的是 pilot。"),
            es("basic", "写出“地铁”的英文单词。", "underground", "地铁在英式英语中常用 underground。",
               accept=["underground", "subway", "metro"]),
            eq("standard", "We go to the park ______ bus.",
               [("A", "by"), ("B", "on the"), ("C", "in")], "A",
               "by + 交通工具（不加冠词）表示乘坐方式。"),
            es("advanced", "用括号内单词的正确形式填空：Fire is ______ (danger). We must be careful.", "dangerous",
               "be 动词后接形容词 dangerous。", accept=["dangerous"])]),

    # ================================================================ 五年级下
    etopic(61, "5下", "全册 核心语法：一般过去时", "一般过去时（was/were 与规则动词）", "语法", "procedural",
           "五下 Module 1—4 开始大量叙述已经发生的事：was/were、-ed 规则变化与 did 构成的疑问句，"
           "是小学阶段最重要的时态之一。",
           ["能正确使用 was/were 描述过去状态", "能构成规则动词过去式并会用 Did…? 提问"],
           ("用括号内单词的正确形式填空：I ______ (visit) my grandma last Sunday.",
            ["last Sunday 表示过去", "visit 是规则动词，加 ed", "所以填 visited"],
            "visited。"),
           ["过去式与现在时混用", "Did 后用过去式（Did you went…）"],
           "先找时间标志词（yesterday、last…、ago），确定用过去时；Did 后动词用原形。",
           ["cne_058"], "2.GR.02",
           [eq("basic", "I ______ my grandma last Sunday.",
               [("A", "visit"), ("B", "visited"), ("C", "visiting")], "B",
               "last Sunday 表示过去，用过去式 visited。"),
            es("basic", "用括号内单词的正确形式填空：They ______ (be) at home yesterday.", "were",
               "yesterday 表示过去，主语 they 接 were。", accept=["were"]),
            eq("standard", "______ you go to the zoo yesterday?",
               [("A", "Do"), ("B", "Did"), ("C", "Were")], "B",
               "实义动词 go 的过去时疑问句用 Did 提问。"),
            es("advanced", "改错（只填正确形式）：Did he watched TV last night? → Did he ______ TV last night?",
               "watch", "Did 后接动词原形。", accept=["watch"])]),

    etopic(62, "5下", "全册 核心语法：一般将来时", "一般将来时（be going to 与 will）", "语法", "procedural",
           "五下谈论周末计划与假期安排：be going to + 动词原形表示计划，will 表示预测或意愿，"
           "两者区别是小学阶段的高频考点。",
           ["能构成 be going to + 动词原形与 will + 动词原形", "能区分“计划”与“临时决定/预测”"],
           ("用括号内单词的正确形式填空：We ______ (go) to the beach next week.",
            ["next week 表示将来", "计划性安排用 be going to", "主语 we 接 are going to go"],
            "are going to go。"),
           ["be going to 后接动词 ing", "will 后加 to（will to go）"],
           "记结构：be going to + 原形（计划）；will + 原形（预测、意愿）。",
           ["cne_061"], "2.GR.03",
           [eq("basic", "We ______ visit the museum tomorrow.",
               [("A", "are going to"), ("B", "is going to"), ("C", "going to")], "A",
               "主语 we 接 are going to + 动词原形。"),
            es("basic", "用括号内单词的正确形式填空：It ______ (be) sunny tomorrow.", "will be",
               "明天天气是预测，用 will be。", accept=["will be", "'ll be"]),
            eq("standard", "Look at the clouds! It ______ rain.",
               [("A", "is going to"), ("B", "was"), ("C", "has")], "A",
               "根据眼前迹象预测，常用 be going to。"),
            es("advanced", "改错（只填正确形式）：She will goes to Beijing. → She will ______ to Beijing.",
               "go", "will 后接动词原形。", accept=["go"])]),

    etopic(63, "5下", "全册 读写：日记与短文阅读", "日记写作与短文阅读", "读写", "application",
           "五下要求写 3—5 句的日记或短文，记录一天的活动与感受；同时能读懂 100 词左右的短文"
           "并完成判断与问答，为初中读写打基础。",
           ["能按“时间—活动—感受”写 3—5 句日记", "能读懂短文并提取 who/what/when 等信息"],
           ("写日记：请写一句“今天我去了公园，玩得很开心。”（用过去时）",
            ["日记用过去时", "去公园 went to the park", "玩得开心 had a good time", "所以是 Today I went to the park and had a good time."],
            "Today I went to the park and had a good time."),
           ["日记用现在时叙述过去的事", "had a good time 写成 have a good time"],
           "日记三句起步：天气/时间一句、活动一句、感受一句。",
           ["cne_062"], "2.DS.01,2.DS.02",
           [eq("basic", "日记中叙述昨天发生的事，应使用（　）。",
               [("A", "一般现在时"), ("B", "一般过去时"), ("C", "现在进行时")], "B",
               "已经发生的事用一般过去时。"),
            es("basic", "补全短语：have a good ______ （玩得开心）。", "time",
               "have a good time 表示玩得开心。", accept=["time"]),
            eq("standard", "阅读：Yesterday was Sunday. Lily went to the zoo with her parents. She saw pandas "
                           "and monkeys. She was very happy. 问：Where did Lily go?",
               [("A", "To the zoo."), ("B", "To the park."), ("C", "To school.")], "A",
               "原文 went to the zoo。"),
            es("advanced", "补全句子：She saw pandas ______ monkeys at the zoo.", "and",
               "两个并列宾语用 and 连接。", accept=["and"])]),
]
