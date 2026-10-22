# Changelog

## 2026-10-22 — 英语细化到教材 Unit 级（63 → 168 个知识点）并补齐高中 7 册

把英语从「册 × 领域」的 63 个模块级知识点，重建为**教材 Unit 级**图谱，并新增**高中英语**（必修第一至第三册、选择性必修第一至第四册）。

### 新增

- **义教段 unit 化**：三至九年级 14 册共 **140 个 Unit → 140 个知识点**（小学每册 12 个，七/八年级 8 个，九年级上 7 个、下 6 个）。`chapter` 改为「三年级上 Unit 1 Hello!」，新增 `level: "unit"`、`book`、`unit_no` 字段；每点 4 题（词汇选择 + 拼写 + 选词填空 + 翻译）。
- **高中英语**：7 册 × 4 个 Unit = **28 个知识点**（`cne_141`–`cne_168`），教材为沪教版（上教版）2020 年审核通过本，单元名逐册核对；`grade` 用 10/11/12 表示高一/高二/高三，前端显示为「高一上」等。
- **高中课标条目** 22 条（`data/cn-highschool-english-curriculum-standards.json`）：必修 13、选择性必修 9；语音 1、词汇 5、语法 9、语篇 4、语用 3，编号 `chs-2017:<1|2>.<PH|VO|GR|DS|PU>.<NN>`，依据《普通高中英语课程标准（2017 年版 2020 年修订）》。22 条全部被引用。
- **先修边**：同册「上一 Unit → 本 Unit」hard、「上一册末 Unit → 本册首 Unit」hard、每册每个领域的首个 Unit 与前面最近的同领域 Unit 之间 soft。英语共 **258 条**（hard 167 / soft 91）。
- **文档**：`docs/english-chapters.md` 重写为 21 册逐 Unit 清单（含 id、领域、课标）；`docs/standards-mapping.md` 新增「9. 英语·高中」一节并重排章节；README、`docs/questions.md`、`diagnose/README.md` 统计同步。

### 变更

- **`scripts/validate.py`**：英语知识点允许 `grade` 10–12；新增 `chs-2017:` 课标 id 校验（前缀、领域代码、册次、域内编号连续）；加载并校验第四个课标文件。
- **`diagnose/engine.js`**：`parseChapter` 新增「册 + Unit N + Unit 名」分支（`三年级上 Unit 1 Hello!`、`必修第一册 Unit 1 Our world`），旧的「全册 + 领域」写法仍兼容。
- **`index.html` / `diagnose/app.js`**：年级标签支持高一/高二/高三（`gradeName()`），`diagnose` 的册次列表补上高中 7 册，「以整章为目标」按当前学科过滤知识点数量。
- **`_builder/`**：删除旧的 `econtent/e3–e9.py`，改为 `eu_primary.py`（96 个 Unit 数据）、`eu_junior.py`（44 个）、`eu_high.py`（28 个手写单元）、`eunits.py`（装配 + 题目生成 + 课标分配）、`ehstandards.py`（高中课标条目）；`ecommon.py` 增加 `eunit()` 构造器。

### 校验

`python3 _builder/build_english.py` → 168 知识点 / 258 边 / 672 题；英语课标映射 350 条（义教 exact 140 / inferred 154，高中 exact 56）；`python3 scripts/validate.py` → `VALIDATION PASSED`（501 节点、618 条边、195 条课标、1956 题）；`python3 scripts/verify_questions.py` → `VERIFICATION PASSED`（auto_verified 917，mismatch 0）；`node tests/test_engine.js` → 69 passed, 0 failed（新增英语 Unit 章节解析用例）。

### 说明

- 英语由 63 个模块级点变为 168 个 Unit 级点，`cne_001`–`cne_168` 的含义随之改变（旧 id 不再指向同一知识点），外部引用如需稳定标识请以最新 `docs/english-chapters.md` 为准。
- 义教段题目由单元数据（核心词、重点句、译文）自动生成，同一 Unit 内题式统一；高中段题目逐题编写。均未经教师审核。

## 2026-10-22 — 新增学科：沪教版英语 3-9 年级（63 个知识点）

在数学（1-9 年级）图谱之外，按同一套数据格式新建**沪教版英语**知识图，覆盖三至九年级 14 册，沿用 `topics + dependencies + standards + questions + diagnose` 结构，英语与数学**各自成图、互不连边**。

### 新增

- **知识点** 63 个（`cne_001`–`cne_063`，`subject: "english"`）：三年级上 2 / 下 3、四年级上 2 / 下 3、五年级上 2 / 下 3、六年级上 6 / 下 6、七年级上 6 / 下 6、八年级上 7 / 下 5、九年级上 7 / 下 5。领域为 **语音 10、词汇 13、语法 23、日常表达 7、读写 10**。
- **先修边** 61 条（hard 60 / soft 1）：英语内部连边，起点为三年级「26 个字母与常见字母组合」，终点为九年级「中考书面表达」；六年级按五四学制预备班处理，作为初级英语的第二个入口。
- **课标条目** 55 条（`data/cn-english-curriculum-standards.json`）：一级（3-4 年级）12、二级（5-6 年级）19、三级（7-9 年级）24；按语言知识领域分为 语音 8、词汇 10、语法 19、语篇 9、语用 9；编号 `ces-2022:<学段>.<PH|VO|GR|DS|PU>.<NN>`，为本项目自编编号。55 条全部被引用，63 个知识点 100% 映射（104 条，均 exact）。
- **题库** 252 题（每点 4 题：choice 126、short 126；basic 126、standard 63、advanced 63）。**只出笔试题**（选择、拼写、填空、词形变化、短文理解），**不出听力与口语**；短答题普遍带 `accept` 等价写法。
- **构建脚本**：`_builder/estandards.py`（课标条目）、`_builder/ecommon.py`（构造器，自动派生诊断题）、`_builder/econtent/e3.py`–`e9.py`（14 册内容与题库）、`_builder/build_english.py`（可重复运行，只替换 `subject == "english"` 的数据，不动数学）。
- **文档**：新增 `docs/english-chapters.md`（各册单元 + 知识点清单）；README 新增英语教材/课标章节与统计；`docs/standards-mapping.md` 增加英语课标对齐一节；`docs/questions.md` 更新题库统计与英语题型说明。

### 变更

- `scripts/validate.py`：`subject` 分流校验（数学 `cnm_*` + 四个数学领域 + 年级 1–9；英语 `cne_*` + 五个英语领域 + 年级 3–9）；课标 id 同时接受 `cms-2022:`（数学）与 `ces-2022:`（英语），英语条目校验 `stage`/`theme`/领域编号连续性；加载并合并第三个课标文件；题 id 前缀接受 `cne_`；「可自动判分」口径改为除 `self` 外全部可判分（numeric + choice + short）。
- `index.html`：新增**数学 / 英语**学科切换，领域与年级下拉按学科动态生成；标题改为「沪教版中小学知识图谱（数学 1-9 年级 · 英语 3-9 年级）」。
- `diagnose/`：开始页新增学科切换，知识点列表按学科过滤；`?target=cne_*` 自动切到英语；`engine.js` 的 `parseChapter` 支持英语「册 + 全册 + 领域：话题」的章节写法，`chapter` 参数仍可用。
- `diagnose/index.html`：标题与说明同步两科。

### 版本说明（关于“2024 版课标”）

沪教版《英语》依据**《义务教育英语课程标准（2022 年版）》**修订，**2024 年**经国家教材委员会专家委员会审核通过。教育部现行英语课标是 2022 年版，**不存在“2024 年版英语课标”**。数据中因此分开标注：`source.year = 2022`（课标）、`source.textbook_year = 2024`（教材审定）。

### 校验

`python3 _builder/build_english.py` → 63 知识点 / 61 边 / 252 题；`python3 scripts/validate.py` → `VALIDATION PASSED`（396 个节点、421 条边、173 条课标、1536 题）；`python3 scripts/verify_questions.py` → `VERIFICATION PASSED`（auto_verified 917，mismatch 0）；`node tests/test_engine.js` → 69 passed, 0 failed（新增英语 Unit 章节解析用例）。

## 2026-10-22 — 扩展到初中：六至九年级（沪教版五四学制，28 章）

在小学（1-5 年级）图谱的基础上，按同一套数据格式补齐**沪教版初中数学 8 册 28 章**，形成 1-9 年级贯通的先修图。

### 新增

- **知识点** 164 个（`cnm_158`–`cnm_321`）：六年级上 25、六年级下 26、七年级上 24、七年级下 20、八年级上 20、八年级下 21、九年级上 15、九年级下 13。覆盖数的整除、分数、比和比例、圆和扇形、有理数、一次方程（组）与不等式（组）、线段与角的画法、长方体、整式、分式、图形的运动、实数、相交线平行线、三角形、平面直角坐标系、二次根式、一元二次方程、正比例与反比例函数、几何证明、一次函数、代数方程、四边形（含平面向量）、概率初步、相似三角形、锐角三角比、二次函数、圆与正多边形、统计初步。
- **先修边** 169 条，其中 20 余条跨学段指向小学知识点（如 `cnm_183 有理数` ← `cnm_147 正数与负数`、`cnm_179 圆的周长` ← `cnm_113 圆的初步认识`、`cnm_261 函数的概念` ← `cnm_135 用字母表示数`）。
- **第四学段课标条目** 54 条（`data/cn-junior-curriculum-standards.json`，数与代数 21、图形与几何 23、统计与概率 6、综合与实践 4），编号 `cms-2022:4.<领域>.<序号>`；初中 164 个知识点 100% 映射（172 条，均 exact），54 条全部被引用。**条目为归纳表述（verbatim=false），未与教育部 PDF 逐页核对，页码“待核”。**
- **题库** 656 题（每点 4 题：numeric 492、choice 164；basic 328、standard 164、advanced 164），数值题全部带 `verify` 表达式，机器核验 mismatch 0。
- **辅导四件套** 每个初中知识点都有 `tutoring`（要点、例题与步骤、常见错误、辅导建议），诊断题的题干与答案直接取第 1 题，二者不会再不一致。
- **构建脚本**：`_builder/junior_standards.py`（课标条目）、`_builder/jcommon.py`（知识点构造器）、`_builder/jcontent/j6a.py`–`j9b.py`（8 册内容）、`_builder/build_junior.py`（可重复运行的合并脚本，只替换 grade≥6 的内容，不动小学数据）。
- **文档**：`docs/junior-chapters.md` 章节目录与知识点清单；README 增加初中教材/课标/统计章节；`docs/standards-mapping.md` 增加第四学段映射说明。

### 变更

- `scripts/validate.py`：`grade` 允许 1–9；同时校验 `data/cn-junior-curriculum-standards.json` 并与小学课标条目合并使用；按年级统计改为动态输出。
- `index.html`：标题与说明改为“中小学（1-9 年级）”；`GRADE_ZH` 补充六至九；年级筛选新增 6 上–9 下 8 项。
- `diagnose/app.js`：`VOLUMES` 扩到 18 册，诊断工具可按初中章节整章筛查；“chapter 参数”示例补充初中格式。
- `diagnose/index.html`：标题与说明同步。

### 校验

`python3 scripts/validate.py` → `VALIDATION PASSED`（333 个节点、360 条边、118 条课标、1284 题）；`python3 scripts/verify_questions.py` → `VERIFICATION PASSED`（auto_verified 917，mismatch 0）；`node tests/test_engine.js` → 69 passed, 0 failed（新增英语 Unit 章节解析用例）。

## 2026-10-21 — 仓库迁移至 momoheal/studyhard

- 独立仓库落地：<https://github.com/momoheal/studyhard>，主分支 `main` 即本项目完整历史（原 fork 自 `momoheal/cn-math-taxonomy`，现作为独立项目维护）。
- 新增 `.nojekyll`，使 GitHub Pages 发布时不忽略 `_builder/` 等以下划线开头的目录。
- README 增加「仓库与在线访问」章节（Pages 地址、开启方式、本地 `http.server` 说明）。`README` 与 `CHANGELOG` 中指向原仓库作为“本仓库”的表述改为上游来源表述。
- 许可证说明补充迁移细节：新仓库创建时 GitHub 自动生成的 Apache-2.0 `LICENSE` 已被覆盖为 CC BY-NC 4.0。

## 2026-10-21 — 沪教版小学数学辅导版（1-5年级·五四学制）首版

从原 [中国初中数学知识图谱（七-九年级，人教版）](https://github.com/momoheal/cn-math-taxonomy) fork 并重做内容域，升级为“知识图谱诊断 + 课本同步辅导”体系。

### 新增

- **课本目录**：严格对齐沪教版小学数学五四学制 10 册目录
  - 一年级上/下：采用**2024年审定版**（上海教育出版社，李大潜主编，教育部2024年8月教学用书目录，2024秋启用），含“我是小学生”“认识图形”等入学适应内容；
  - 二至五年级：采用**现行九年义务教育课本（试用本）**目录（上海教育出版社/少年儿童出版社），与学校在用教材一致；
  - 章节统一书写为“年级册 + 单元 + 小节 + 课时”（如 `一年级上 第三单元 10以内的数 3.1 1-5的认识`），共 10 册、60 个单元。
- **知识点**：157 个正式知识点 + 12 个学前外部节点 = 169 个节点；按领域（数代103/几何33/综合15/统计6）、册次（1上18/1下16/2上18/2下18/3上16/3下16/4上14/4下10/5上17/5下14）、类型（procedural72/conceptual54/application20/reasoning10/modeling1）分布。
- **先修边**：191 条（hard163/soft28），平均先修1.22，覆盖同册递进与跨册衔接（如“两位数加减 → 一位数乘 → 两位数乘”），根节点为学前外部，无需 `root_reason`。
- **课标对齐**：新建 `data/cn-curriculum-standards.json` 64 条（第一学段1-2年级 20条、第二学段3-4年级25条、第三学段5-6年级19条，对应上海五四五年级），按 `cms-2022:<学段>.<领域>.<序号>` 编号；正式点100%映射（184条，均为exact）。
- **辅导四件套**：每个正式点新增 `tutoring` 字段：`key_points(3)` 要点精讲、`worked_example{problem, steps, answer}` 例题精讲、`common_mistakes(2)` 常见错误、`coaching_tip(1)` 家长话术；浏览页 `index.html` 中直接展开，并提供“去做4题小测”跳转。内容按知识点逐条维护在 `_builder/content/g1.py`～`g5.py`，由 `_builder/apply_content.py` 合并。
- **题库**：每个正式点 4 题（628题：numeric425/choice197/short6；basic314/standard157/advanced157），`verify` 表达式 425 题通过，mismatch0，unverifiable203（文字选项与少量带单位short题）。
- **诊断联动**：结果页根因卡片新增“查看辅导卡”链接至浏览页锚点；URL参数与题量/种子逻辑保持不变。

### 变更

- **校验脚本**：`scripts/validate.py` 支持小学学段（grade 1-5，外部学前/小学，领域不变，章节点名支持“单元”与多级标题）；`scripts/verify_questions.py` 复用，验证规则不变（numeric parse 适配小数/分数，short题不计auto_share）。
- **浏览页**：标题、筛选（一年级上…五年级下）、分组、标签（学前先备）、辅导卡渲染、同步练习入口；`parseChapter` 正则支持“第X单元/章”与含空格的小节名。
- **诊断页**：`VOLUMES` 更新为10册，`parseChapter` 同步，文案改为小学辅导版；`engine.js` 核心算法未变，仅章节点解析适配小学章节格式。
- **测试**：`tests/test_engine.js` 适配新数据规模（169节点/191边/64课标条目），阈值调整（cases≥400、numeric>200、withPrereq>10），目标示例改为 `cnm_050`（正方体与长方体的初步认识），章名示例改为“一年级上 第三单元”。

### 文档

- 重写 `README.md`、`docs/standards-mapping.md`、`docs/questions.md`、`diagnose/README.md` 为小学辅导版；
- `CHANGELOG.md` 记录混合版（hybrid_2024）策略与过渡说明；
- `LICENSE` 保持 CC BY-NC 4.0。

### 已知待办

- 待二至五年级2024版教材发布后，逐册更新目录与知识点拆分；
- 辅导四件套与题库需沪教版一线教师审核与补充真实学生错因；
- 诊断中“不稳不回溯”策略与学前根因定位可按实测调整。

---

此前为初中版变更（见原仓库 CHANGELOG），本版起独立演进。
