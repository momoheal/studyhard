# 题库说明（data/questions.json）

每个正式知识点（510 个：数学小学 157、数学初中 164、英语义教 154、英语高中 35）配套 4 题起，共 3320 题，供诊断工具“每点最多 2 题”出题策略使用。题目由 AI 基于课本生成，**未经教师审核**，正确性主要靠机器核验。

> 英语题只出**笔试题**（选择、拼写、选词填空、翻译、语篇语法填空、连词成句、情景问答、中译英），**不出听力与口语题**；数学 4 题/点，英语 Unit 4 题起（小学约 9—10 题、初中 11 题、高中 17 题），每册另有 1 套 10 题的册末 mini 卷。短答题普遍带 `accept` 等价写法，答案唯一的填空题带 `exact: true`。

## 1. 格式

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | `<topicId>_qN`，如 `cnm_052_q1`；`_q1` 题干与 `topics.json` 的 `diagnostic_question` 一致 |
| `topicId` | 是 | 知识点 id（正式点） |
| `difficulty` | 是 | `basic` 基础（课本例题水平一步计算）、`standard` 标准（2步）、`advanced` 提高（多步或易错） |
| `type` | 是 | `numeric` 数值题（答案可解析为数）、`choice` 选择题、`short` 短答（带单位/时间的非纯数字答案） |
| `prompt` | 是 | 中文题干，纯文字（几何条件用文字描述，不依赖配图） |
| `answer` | 是 | 字符串：numeric 为数字（整数/小数/分数）、choice 为选项字母、short 为短答案（如“10角”“9:05”） |
| `choices` | choice 必填 | 3-4 个选项 `[{key, text}]`，key 依次 A、B、C、D |
| `explanation` | 是 | 1-2 句中文解析 |
| `verify` | 否 | Python 表达式，用于机器核验（见下） |
| `accept` | 否 | 等价答案列表 |
| `unordered` | 否 | 多答案顺序无关时为 true（本版暂未使用） |
| `exact` | 否 | 仅 `short` 题可用；为 `true` 表示答案唯一（首字母填空、语篇填空的每个空、词形填空），判题器对不上即判 `wrong`，不落到“自评” |

## 2. 统计

- 总数 **3320 题**，覆盖 510 个正式点，数学每点 4 题、英语每点 4—17 题（平均 6.5 题）。
  - 数学小学 628 题（numeric 425，choice 197，short 6；basic 314，standard 157，advanced 157）。
  - 数学初中 656 题（numeric 492，choice 164；basic 328，standard 164，advanced 164）。初中的 basic/standard/advanced 比例为 2:1:1，每点至少两道 basic。
  - 英语义教 1490 题（154 个知识点：choice 392、short 1098；basic 723、standard 487、advanced 280）。
  - 英语高中 546 题（35 个知识点：choice 112、short 434；basic 168、standard 266、advanced 112）。
  - 英语册末卷 21 套共 210 题（每套 8 选择 + 2 短答），已含在上面两组里。
- 按 type：numeric 917，choice 865，short 1538；可自动判分（numeric + choice + short）占 100%，其中 951 道 `exact` 短答题可由判题器直接判对错。
- 按 difficulty：basic 1533，standard 1074，advanced 713；数学每点含 basic 与 standard，英语短文的空按「前 2 空 basic、其后 standard、末尾约 30% advanced」分配。
- 英语题不依赖配图与音频：
  - 基础 4 题（每 Unit）由该 Unit 的核心词、重点句与译文生成（词汇选择、拼写、选词填空、翻译）；
  - 扩充题按学段手写：小学「首字母填空短文（4—5 空）+ 连词成句」、初中「语篇语法填空（6 空）+ 情景问答」、高中「语篇语法填空（10 空）+ 中译英 3 句」；
  - 语篇短文的每个空各自成一道 `short` 题（题干带全篇短文与本题提示，解析给出全篇答案），因此题量增长快于篇数；
  - 高中 Unit 的 4 道基础题按单元语法点与读写重点单独编写。
- choice 正确选项分布大致均匀。
- 初中的 `verify` 表达式覆盖全部数值题（492 题），用到 `sqrt`、`sin/cos/tan`（弧度制）、`round`、`Fraction`、列表推导式等受限名字，机器核验 mismatch 0。
- 英语题不带 `verify`（语言题无法用表达式核验），与数学的文字类选择题一样计入 `unverifiable`，依赖 `accept` 列表与人工审读。

## 3. 核验方法

### 3.1 自动核验（`python3 scripts/verify_questions.py`）

numeric 与 choice 题可带 `verify` 表达式，脚本在受限环境（AST 白名单，仅允许四则、比较、少数函数如 `round`）中求值，再与 `answer` 比较：

- numeric：结果与 `answer` 按数值比较（分数精确，浮点容差 1e-9）。多答案支持 `unordered`。
- choice：结果与正确选项文字按数值或字符串比较，并检查无双解。

当前结果（`data/verification_report.json`）：

| 项 | 数量 |
|---|---|
| auto_verified | 917 |
| mismatch | 0 |
| unverifiable | 2403（choice 865 + short 1538，含全部英语题） |

`mismatch 0` 表示有 `verify` 的题目均通过；`unverifiable` 为无 `verify` 的题目（主要为干扰项为文字的选择题与带单位/时间的 short 题），依赖人工审核或后续第二遍独立复核。

### 3.2 格式校验（`python3 scripts/validate.py`）

检查题 id 唯一、topicId 存在且非外部、`difficulty/type` 合法、choice 选项格式、`numeric` 答案可解析、每点 ≥3 题且含 basic+standard、`q1` 与诊断题一致等；题 id 前缀同时接受 `cnm_`（数学）与 `cne_`（英语）。

## 4. 局限

- **无教师审核**：干扰项、难度标注均为 AI 主观，未用学生数据校准。
- **题量与重复**：数学每点仅 4 题，英语 Unit 4—17 题；诊断每点最多 2 题，重测仍可能重复，选择题有猜对概率。
- **无配图题**：几何题用文字描述数量关系，无作图与证明题。
- **verify 同源风险**：`verify` 与答案同为 AI 生成，若算法同错则无法暴露；已通过统计与多样化题型尽量降低。
- **short 题**：带单位（“10角”）、时间（“9:05”）、角度（“90°”）等答案为 short 类型，判题时需人工或诊断工具的文本规范化逻辑辅助，不在自动核验范围内。
- **英语题**：判题按大小写、空格、标点规范化后精确匹配，`accept` 覆盖同义写法（如 `I’m` / `I am`、`doesn't` / `does not`）；标了 `exact: true` 的填空题对不上即判错，翻译、情景问答、连词成句只做宽松匹配并回落到自评，**不能代替教师批改**。
- **多空短文重复题干**：同一篇短文的 5/6/10 个空各自成题，题干会重复整篇短文（为了让每个空可精确判分）；若需要“整篇一次做完”的卷面视图，可后续在页面层组装。
- **册末卷**：每套 10 题，覆盖该册各 Unit 的核心词与语法点，属 mini 卷，**不能替代单元测验或期末考试**。
