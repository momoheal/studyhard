# -*- coding: utf-8 -*-
"""沪教版英语 三年级上、下册（小学三起点；依据 2022 年版课标一级要求编写）。

三上 Module 1—4（12 个单元）：
Getting to know you（Hello! / How are you? / Are you Kitty?）、
My family, my friends and me（My friends / My family / Me）、
Places and activities（In the classroom / At the fruit shop / In my room）、
The world around us（Numbers / Small animals / The four seasons）
三下 12 个单元：Colours / Tastes / Sounds / Animals in the zoo / Toys / Food and drinks /
Hobbies / Happy birthday! / A day on the farm / Funny cartoons / Mother's Day / Three little pigs
"""

from ecommon import eq, es, etopic

ROOT = ("三年级是沪教版英语（三起点）的第一年，按零起点处理，前面没有更早的英语知识点。"
        "本组知识点是全图英语部分的起点。")

TOPICS = [

    # ================================================================ 三年级上
    etopic(49, "3上", "全册 语音：26 个字母与常见字母组合", "26 个字母与常见字母组合", "语音", "conceptual",
           "三上 Unit 1—12 从字母与问候语起步：Hello、hi、name、cat、dog、sun、moon 等，"
           "本知识点梳理字母大小写、元音字母的基本读音与 sh、ch、th 的常见读法。",
           ["能认读并书写 26 个字母的大小写", "能读准 a、e、i、o、u 在单词中的常见读音"],
           ("判断：单词 cake 中字母 a 的读音与 cat 中的 a 是否相同？",
            ["cake 中 a 读 /eɪ/", "cat 中 a 读 /æ/", "两者不同", "所以不相同"],
            "不相同。"),
           ["把字母 b 与 d、p 与 q 写反", "把 cat 中的 a 读成 /eɪ/"],
           "每天边写边读 5 个字母，写完对照示范检查 b/d、p/q 的方向。",
           [], "1.PH.01,1.PH.02",
           [eq("basic", "下列单词中，字母 a 读 /eɪ/ 的是（　）。",
               [("A", "cat"), ("B", "cake"), ("C", "bag")], "B",
               "cake 中 a 读 /eɪ/；cat、bag 中读 /æ/。"),
            es("basic", "字母组合 sh 在单词 she 中读 /ʃ/。请写出一个含 sh 且读 /ʃ/ 的单词。", "she",
               "she、ship、shop、fish 中的 sh 都读 /ʃ/。",
               accept=["she", "ship", "shop", "fish", "shirt", "shoe", "short"]),
            eq("standard", "字母表中排在 m 后面的字母是（　）。",
               [("A", "l"), ("B", "n"), ("C", "o")], "B",
               "字母表顺序为 … l, m, n, o …。"),
            es("advanced", "补全单词：__ range（橙子），首字母是 o。写出完整单词。", "orange",
               "orange 以元音字母 o 开头，前面用 an。", accept=["orange"])],
           root_reason=ROOT),

    etopic(50, "3上", "全册 词汇：问候、家庭、教室与数字", "主题词汇与短语（问候·家庭·教室·数字）", "词汇", "conceptual",
           "三上四个 Module 的话题词：hello、goodbye、friend、father、mother、sister、"
           "classroom、desk、chair、book、apple、banana、one—ten、cat、dog、spring、summer 等。",
           ["能认读并抄写本册核心词", "能在图片提示下说出单词并注意单复数"],
           ("看图说词：图上有两只猫，用英语怎么说？",
            ["cat 的复数是 cats", "数量为二", "所以是 two cats"],
            "two cats。"),
           ["复数漏加 s（two cat）", "a 与 an 用错（a apple）"],
           "把单词和图片贴在一起记，每天用 5 个词说一句话。",
           ["cne_049"], "1.VO.01,1.VO.02",
           [eq("basic", "— What's this? — It's ______ apple.",
               [("A", "a"), ("B", "an"), ("C", "two")], "B",
               "apple 以元音音素开头，用 an。"),
            es("basic", "写出“三”的英文单词。", "three", "数字 3 的英文是 three。", accept=["three"]),
            eq("standard", "There are two ______ in the picture.",
               [("A", "cat"), ("B", "cats"), ("C", "a cat")], "B",
               "two 后接可数名词复数 cats。"),
            es("advanced", "补全单词：cl__ssroom（教室）。写出完整单词。", "classroom",
               "classroom = class + room。", accept=["classroom"])]),

    # ================================================================ 三年级下
    etopic(51, "3下", "全册 词汇：颜色、味道、动物与玩具", "主题词汇与短语（颜色·味道·动物·玩具）", "词汇", "conceptual",
           "三下 Unit 1—12 的话题词：red、yellow、blue、sweet、sour、tiger、monkey、"
           "doll、ball、cake、juice、hobby、birthday、farm、pig、duck 等。",
           ["能认读并抄写本册核心词", "能用形容词描述颜色、味道与感受"],
           ("用英语说“这个苹果是甜的。”",
            ["苹果是 the apple / this apple", "甜的是 sweet，作表语", "所以是 The apple is sweet."],
            "The apple is sweet."),
           ["把形容词放在名词后（apple sweet）", "sour 与 sweet 混用"],
           "按颜色、味道、动物、玩具四类做单词卡片，正面英文、背面中文。",
           ["cne_050"], "1.VO.01,1.VO.02",
           [eq("basic", "The lemon is ______ . I don't like it.",
               [("A", "sweet"), ("B", "sour"), ("C", "red")], "B",
               "柠檬是酸的，用 sour。"),
            es("basic", "写出“蓝色”的英文单词。", "blue", "蓝色是 blue。", accept=["blue"]),
            eq("standard", "I have a ______ . It can jump and it likes bananas.",
               [("A", "monkey"), ("B", "duck"), ("C", "tiger")], "A",
               "会跳、爱吃香蕉的是 monkey。"),
            es("advanced", "用括号内单词的正确形式填空：Look at the two ______ (duck) in the river.", "ducks",
               "two 后接复数 ducks。", accept=["ducks"])]),

    etopic(52, "3下", "全册 核心语法：be 动词与 can", "be 动词与情态动词 can", "语法", "procedural",
           "三下 Unit 3 Sounds、Unit 7 Hobbies 中反复出现 I am… / You are… / She is… 与 "
           "I can swim. / Can you…? 是本册最重要的两个句型。",
           ["能正确使用 am、is、are 构成肯定句、否定句与一般疑问句", "能用 can 表达能力并构成疑问句与否定句"],
           ("填空：______ you swim? — Yes, I can.",
            ["问“你会游泳吗”，用 can 提前", "主语 you 用 Can", "所以填 Can"],
            "Can。"),
           ["用 Do you can swim?", "can 后加 to（can to swim）"],
           "记两句口诀：be 动词看主语（I am / you are / he is）；can 后面跟原形。",
           ["cne_051"], "1.GR.01,1.GR.03",
           [eq("basic", "______ you swim? — Yes, I can.",
               [("A", "Do"), ("B", "Can"), ("C", "Are")], "B",
               "问能力用 Can you…?，答语 Yes, I can. 印证。"),
            es("basic", "用 am、is 或 are 填空：I ______ a pupil.", "am",
               "主语 I 搭配 am。", accept=["am"]),
            eq("standard", "She ______ dance, but she can sing.",
               [("A", "can"), ("B", "can't"), ("C", "isn't")], "B",
               "but 表示转折，前面应是不能跳舞 can't。"),
            es("advanced", "改错（只填正确形式）：He can plays football. → He can ______ football.", "play",
               "can 后接动词原形。", accept=["play"])]),

    etopic(53, "3下", "全册 日常表达：问候、介绍与生日祝福", "问候、介绍与生日祝福", "日常表达", "application",
           "三上 Unit 1—3、三下 Unit 8 Happy birthday! 构成本册的交际主线："
           "Hello! / How are you? / This is my friend. / Happy birthday! / Thank you.",
           ["能用 Hello、Good morning、How are you? 完成问候与应答", "能用 This is… 介绍他人，并表达生日祝福与感谢"],
           ("— How are you? — ______",
            ["问候健康近况", "常用答语 I'm fine, thank you.", "所以答 I'm fine, thank you."],
            "I'm fine, thank you."),
           ["How are you? 答成 How are you?", "介绍他人用 I am…（应为 This is…）"],
           "两人一组每天做一次三句问候对话，直到不用想就能说出。",
           ["cne_051"], "1.PU.01,1.PU.02,1.DS.01",
           [eq("basic", "— How are you? — ______",
               [("A", "I'm fine, thank you."), ("B", "I'm nine."), ("C", "It's red.")], "A",
               "How are you? 问候健康，答 I'm fine, thank you."),
            es("basic", "别人说 Happy birthday! 时，常用答语是 Thank ______ .", "you",
               "Thank you. 表示感谢。", accept=["you"]),
            eq("standard", "介绍你的朋友给妈妈，应该说（　）。",
               [("A", "This is my friend, Tom."), ("B", "I am Tom."), ("C", "How are you, Tom?")], "A",
               "介绍他人用 This is…。"),
            es("advanced", "补全对话：— Good morning, Miss Li. — Good ______ , Tom.", "morning",
               "早晨问候语为 Good morning。", accept=["morning"])]),
]
