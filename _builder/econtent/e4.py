# -*- coding: utf-8 -*-
"""沪教版英语 四年级上、下册（小学三起点；依据 2022 年版课标一级要求编写）。

四上 12 个单元：Meeting new people / Can you swim? / Are you happy? /
Do you have any cousins? / My friends / My parents / At school / At the shop /
At home / Around my home / Shapes / Weather
四下：Touch and feel / Smell and taste / Look and say 等感官与生活话题单元
"""

from ecommon import eq, es, etopic

TOPICS = [

    # ================================================================ 四年级上
    etopic(54, "4上", "全册 语音：字母组合与单词重音", "字母组合读音与单词重音", "语音", "procedural",
           "四上 Unit 7 At school、Unit 12 Weather 中出现 chair、teacher、weather、thirsty 等词，"
           "本知识点练习 ch、th、-er 的读音与双音节词的重音。",
           ["能读准 ch /tʃ/、th /θ/ 或 /ð/ 的常见词", "能读准双音节词的重音位置"],
           ("判断：单词 teacher 的结尾 -er 读什么？",
            ["teacher 结尾是 -er", "在词尾通常弱读为 /ə/", "所以读 /ə/"],
            "/ə/。"),
           ["把 th 一律读成 /s/", "把 -er 读成重读的 /ɜː/"],
           "把 ch、th、sh 三类词各抄 5 个，边读边比较口型。",
           ["cne_049"], "1.PH.02",
           [eq("basic", "下列单词中，th 读 /θ/ 的是（　）。",
               [("A", "this"), ("B", "three"), ("C", "that")], "B",
               "three、think、thank 中 th 读 /θ/；this、that 中读 /ð/。"),
            es("basic", "单词 teacher 中 -er 通常读作 /______ /（填一个音标符号）。", "ə",
               "词尾 -er 弱读为 /ə/。", accept=["ə", "/ə/"]),
            eq("standard", "下列单词重音在第一个音节的是（　）。",
               [("A", "today"), ("B", "weather"), ("C", "begin")], "B",
               "weather 是双音节词，重音在首音节。"),
            es("advanced", "补全单词：t__cher（教师）。写出完整单词。", "teacher",
               "teacher 由 teach + er 构成。", accept=["teacher"])]),

    etopic(55, "4上", "全册 词汇：外貌、能力、情绪与天气", "主题词汇与短语（外貌·能力·情绪·天气）", "词汇", "conceptual",
           "四上话题围绕“认识新朋友”：tall、short、thin、strong、happy、sad、angry、"
           "cousin、parents、swim、skate、sunny、rainy、windy、cloudy 等。",
           ["能认读并拼写本册核心词", "能用形容词描述外貌与情绪，用 -y 构成天气形容词"],
           ("用括号内单词的正确形式填空：It is ______ (sun) today.",
            ["be 动词后需要形容词", "sun 加 y 变 sunny，注意双写 n", "所以填 sunny"],
            "sunny。"),
           ["sunny 漏写一个 n", "happy 与 sad 用错场合"],
           "天气词按“名词 + y”一组记：sun→sunny、rain→rainy、wind→windy、cloud→cloudy。",
           ["cne_050"], "1.VO.01,1.VO.02",
           [eq("basic", "It is ______ today. We can't go out.",
               [("A", "rainy"), ("B", "rain"), ("C", "rains")], "A",
               "be 动词后接形容词 rainy。"),
            es("basic", "写出“快乐的”英文单词。", "happy", "happy 表示快乐。", accept=["happy"]),
            eq("standard", "My ______ are my father and my mother.",
               [("A", "parents"), ("B", "cousins"), ("C", "friends")], "A",
               "父亲和母亲是 parents。"),
            es("advanced", "用括号内单词的正确形式填空：He is ______ (tall) than his brother.", "taller",
               "than 提示比较级，tall 加 -er。", accept=["taller"])]),

    # ================================================================ 四年级下
    etopic(56, "4下", "全册 词汇：感官、形状与购物", "主题词汇与短语（感官·形状·购物）", "词汇", "conceptual",
           "四下 Unit 1—3 以五种感官为主线：touch、feel、soft、hard、smell、taste、sweet、sour、"
           "look、shape、circle、square、triangle、shop、buy 等。",
           ["能认读并拼写感官与形状类词汇", "能用 It feels/smells/tastes… 描述事物"],
           ("用英语说“这个包摸起来很软。”",
            ["主语 the bag", "feel 表示“摸起来”，第三人称单数 feels", "所以是 The bag feels soft."],
            "The bag feels soft."),
           ["feel 后接副词（feels softly）", "形状词与物品搭配错误"],
           "五种感官各写一句：It looks / sounds / smells / tastes / feels…。",
           ["cne_051"], "1.VO.01,1.VO.02",
           [eq("basic", "The ice cream ______ sweet.",
               [("A", "tastes"), ("B", "taste"), ("C", "tasting")], "A",
               "主语是第三人称单数，taste 加 s。"),
            es("basic", "写出“圆形”的英文单词。", "circle", "circle 表示圆形。", accept=["circle"]),
            eq("standard", "The stone is ______ . I can't break it.",
               [("A", "soft"), ("B", "hard"), ("C", "sweet")], "B",
               "石头是硬的，用 hard。"),
            es("advanced", "补全句子：The soup ______ (smell) good.", "smells",
               "主语 the soup 第三人称单数，smell 加 s。", accept=["smells"])]),

    etopic(57, "4下", "全册 核心语法：名词复数与 there be", "名词复数与 there be 句型", "语法", "procedural",
           "四下 Unit 5—7 描述家里的物品与学校场所，大量使用 There is / There are 与名词复数，"
           "是本册最重要的语法点。",
           ["能正确构成名词复数（含 -s、-es、不规则变化）", "能根据名词单复数选用 There is 或 There are"],
           ("填空：There ______ two books on the desk.",
            ["主语 two books 是复数", "复数用 There are", "所以填 are"],
            "are。"),
           ["用 There is two books", "以 s、x、ch、sh 结尾的名词漏加 es"],
           "先看名词单复数，再决定 is 还是 are；把 box→boxes、bus→buses 单独抄写。",
           ["cne_052"], "1.GR.02",
           [eq("basic", "There ______ two books on the desk.",
               [("A", "is"), ("B", "are"), ("C", "be")], "B",
               "two books 是复数，用 There are。"),
            es("basic", "写出 box 的复数形式。", "boxes", "以 x 结尾加 -es。", accept=["boxes"]),
            eq("standard", "There ______ a cat and two dogs in the garden.",
               [("A", "is"), ("B", "are"), ("C", "have")], "A",
               "there be 就近原则，靠近的是 a cat，用 is。"),
            es("advanced", "写出 child 的复数形式。", "children", "child 的复数是不规则形式 children。",
               accept=["children"])]),

    etopic(58, "4下", "全册 核心语法：一般现在时（like / have / go）", "一般现在时与动词第三人称单数", "语法", "procedural",
           "四下谈及爱好与日常：I like… / She likes… / He has… / We go to school by bus. "
           "第三人称单数是本册的核心难点。",
           ["能正确使用一般现在时描述习惯与喜好", "能正确给动词加 -s 或 -es"],
           ("用括号内单词的正确形式填空：She ______ (like) drawing.",
            ["主语 she 是第三人称单数", "一般现在时动词加 s", "所以填 likes"],
            "likes。"),
           ["第三人称单数漏加 s", "以 o、s、x、ch、sh 结尾的动词漏加 es（goes、watches）"],
           "记规则：一般加 s；s/x/ch/sh/o 结尾加 es；辅音字母 + y 变 i 加 es。",
           ["cne_057"], "1.GR.04,1.DS.02",
           [eq("basic", "She ______ drawing very much.",
               [("A", "like"), ("B", "likes"), ("C", "liking")], "B",
               "主语 she 第三人称单数，like 加 s。"),
            es("basic", "用括号内单词的正确形式填空：He ______ (go) to school by bus.", "goes",
               "go 以 o 结尾，第三人称单数加 es。", accept=["goes"]),
            eq("standard", "下列句子正确的是（　）。",
               [("A", "My sister watch TV every day."), ("B", "My sister watches TV every day."),
                ("C", "My sister watchs TV every day.")], "B",
               "watch 以 ch 结尾，第三人称单数加 es。"),
            es("advanced", "用括号内单词的正确形式填空：Tom ______ (have) a new bike.", "has",
               "have 的第三人称单数是不规则形式 has。", accept=["has"])]),
]
