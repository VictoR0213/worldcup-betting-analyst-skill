# World Cup Betting Analyst

Evidence-backed World Cup football analysis for Chinese Sporttery-style markets, built as a Codex Skill.

[![Codex Skill](https://img.shields.io/badge/Codex%20Skill-worldcup--betting--analyst-red)](worldcup-betting-analyst/SKILL.md)
[![Markets](https://img.shields.io/badge/Markets-WDL%20%7C%20Handicap%20%7C%20Score%20%7C%20Goals%20%7C%20Parlay-blue)](#core-capabilities)
[![Output](https://img.shields.io/badge/Output-Chat%20%7C%20JSON%20Schema-2ea44f)](worldcup-betting-analyst/references/output-schema.md)
[![Risk Control](https://img.shields.io/badge/Betting-Risk--Aware-black)](#risk-and-responsible-use)
[![Language](https://img.shields.io/badge/Language-%E4%B8%AD%E6%96%87%20%7C%20English-lightgrey)](#english-version)

中文 | [English](#english-version)

---

## 中文版

`worldcup-betting-analyst` 是一个面向世界杯及世界杯周期相关赛事的 Codex Skill，用于生成结构化、证据导向、风险可控的足球赛前分析。它适合处理中国竞彩语境下的胜平负、让球胜平负、比分、总进球、半全场和串关/过关问题。

这个项目的核心目标不是给出“确定性答案”，而是把足球判断、赔率判断和风险判断拆开处理：

- 先判断比赛本身更可能如何发展；
- 再判断当前赔率是否已经充分反映这种预期；
- 最后决定某个选择是否值得单关、是否适合串关，或者是否应该跳过。

## 项目定位

| 维度 | 说明 |
|---|---|
| 使用场景 | 世界杯赛前分析、竞彩玩法拆解、赔率合理性检查、串关组合筛选 |
| 主要用户 | 需要更有纪律地分析比赛和赔率的中文用户 |
| 分析风格 | 证据优先、概率表达、区分强弱信号、明确风险和信息缺口 |
| 输出形态 | 中文聊天回答、结构化 JSON、批量比赛摘要、串关建议 |
| 风险边界 | 不承诺盈利，不鼓励追损，不伪造赔率、伤停、天气或内幕信息 |

## 核心能力

| 模块 | 能力 |
|---|---|
| 胜平负 | 给出 90 分钟常规时间内的胜、平、负概率判断，并说明主要依据 |
| 让球胜平负 | 将让球盘转换成净胜球要求，判断热门方向是否被高估 |
| 比分 | 给出 2-3 个高相关比分候选，并标注高方差风险 |
| 总进球 | 结合节奏、攻防质量、天气、动机和比赛状态判断进球区间 |
| 半全场 | 结合上半场谨慎程度、换人节奏和体能变化给出低置信度参考 |
| 串关/过关 | 只保留证据较强、相关性较低的选项；证据不足时建议不串 |
| 赔率价值 | 将十进制赔率转换为隐含概率，必要时考虑市场水位和边际 |
| 风险控制 | 主动提示伤停、首发、天气、赛程动机、盘口变化等不确定因素 |

## 分析流程

1. 明确比赛背景
   确认赛事阶段、开球时间、场地、城市、当地天气、休息天数、旅行距离和出线/排名动机。

2. 建立赛前足球判断
   综合球队强度、近期状态、伤停停赛、战术对位、教练稳定性、比赛动机和场地因素，形成不看赔率时的初始概率。

3. 对照市场价格
   把赔率转换为隐含概率，检查市场是否已经过度压低热门方向，避免把“更可能发生”和“值得买”混为一谈。

4. 分玩法输出
   对胜平负、让球、比分、总进球、半全场和串关分别给出结论、置信度、理由和风险。

5. 收尾风险提示
   列出信息缺口和可能推翻判断的关键变量，例如临场首发、核心球员伤情、天气突变、盘口异动或轮换动机。

## 安装方式

将 Skill 文件夹复制到本机 Codex skills 目录：

```powershell
Copy-Item -Recurse .\worldcup-betting-analyst $env:USERPROFILE\.codex\skills\
```

重启 Codex 后即可使用：

```text
Use $worldcup-betting-analyst to analyze France vs Brazil for all markets.

$worldcup-betting-analyst 帮我分析今晚世界杯胜平负、让球胜平负、比分、总进球和半全场。

$worldcup-betting-analyst 这三场怎么串更稳一点？如果不值得串，也直接告诉我。
```

## 输出示例

正常聊天输出会优先使用中文，并保持结构紧凑：

```text
结论先行
主方向：主胜略优，但赔率偏低，不建议重仓。
更稳妥选择：让球方向或总进球区间需要结合临场首发确认。

比赛背景
- 开球时间：北京时间 ...
- 场地与天气：...
- 动机：...

概率判断
- 主胜：45%
- 平局：29%
- 客胜：26%

分玩法建议
- 胜平负：主胜，置信度 medium
- 让球胜平负：让平/让负优先观察
- 比分：1-0、1-1、2-1，比分市场高方差
- 总进球：2 球或 3 球
- 半全场：平/胜、平/平，仅低置信度参考

风险与信息缺口
- 首发未确认
- 赔率变化原因未确认
- 天气可能影响比赛节奏
```

如果用户需要 API-ready 或批量预测输出，可以要求 JSON。结构规范见 [`output-schema.md`](worldcup-betting-analyst/references/output-schema.md)，并可使用验证脚本检查：

```powershell
python .\worldcup-betting-analyst\scripts\validate_output.py prediction.json
```

## 文件结构

```text
worldcup-betting-analyst-skill/
├── README.md
├── LICENSE
└── worldcup-betting-analyst/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── data-sources.md
    │   ├── methodology.md
    │   └── output-schema.md
    └── scripts/
        └── validate_output.py
```

| 文件 | 用途 |
|---|---|
| [`SKILL.md`](worldcup-betting-analyst/SKILL.md) | Skill 的核心行为规则、分析流程和安全边界 |
| [`data-sources.md`](worldcup-betting-analyst/references/data-sources.md) | 官方赛程、竞彩数据、球队新闻、天气和历史资料的来源优先级 |
| [`methodology.md`](worldcup-betting-analyst/references/methodology.md) | 概率、赔率价值、置信度和红旗信号的方法说明 |
| [`output-schema.md`](worldcup-betting-analyst/references/output-schema.md) | 单场和多场 JSON 输出格式 |
| [`validate_output.py`](worldcup-betting-analyst/scripts/validate_output.py) | JSON 预测结果验证脚本 |
| [`openai.yaml`](worldcup-betting-analyst/agents/openai.yaml) | Codex/UI 元数据 |

## 数据与证据要求

分析真实或即将开赛的比赛时，必须优先核验当前信息，不依赖旧记忆：

- 官方赛程、比赛阶段、开球时间、场馆和城市；
- 竞彩或用户提供的当前赔率和玩法状态；
- 伤停、停赛、首发倾向、轮换可能和近期状态；
- 当地天气、湿度、风速、降雨概率和场地条件；
- 球队实力、历史表现、战术风格、休息和旅行因素。

如果某项信息无法确认，输出中应明确标注 `unconfirmed`，并下调置信度。

## 适合与不适合

适合：

- 赛前多维度分析；
- 对比概率判断和赔率价格；
- 识别热门低赔是否被压得过低；
- 从多场比赛中筛选少量相对独立的串关候选；
- 生成可验证的 JSON 预测记录。

不适合：

- 保证命中或保证盈利；
- 追损、倍投、借钱下注或超预算下注；
- 没有当前信息时强行给出确定性推荐；
- 把国际赔率伪装成中国竞彩赔率；
- 把比分市场当作低风险主玩法。

## 风险与负责任使用

足球比赛具有高度不确定性，尤其是比分、半全场和串关市场。该 Skill 只提供分析框架和概率判断，不构成投资建议，也不提供任何盈利保证。

请始终遵守以下原则：

- 不追损；
- 不借钱下注；
- 不因为低赔率就认为安全；
- 不把串关当作降低风险的方法；
- 只使用能够承受损失的娱乐预算。

当用户表现出追损、情绪化投注或“必须回本”等风险信号时，Skill 应停止给出投注选择，并建议暂时不下注。

## 灵感与归因

本项目受到以下开源项目和资料的启发：

- [`sahuan14/worldcup-betting-analyst-skill`](https://github.com/sahuan14/worldcup-betting-analyst-skill)：竞彩分析流程和风险控制表达。
- [`jfjelstul/worldcup`](https://github.com/jfjelstul/worldcup)：世界杯历史数据库结构和历史语境参考。
- [`TradingAi666/worldcup2026-prediction-skill`](https://github.com/TradingAi666/worldcup2026-prediction-skill)：结构化输出和预测工作流设计思路。

本仓库当前不重新分发历史数据集。如未来加入派生数据，应保留原始作者署名并遵守对应许可证要求。

## 许可证

请查看 [`LICENSE`](LICENSE)。

---

## English Version

`worldcup-betting-analyst` is a Codex Skill for structured, evidence-backed, risk-aware football analysis during the FIFA World Cup cycle. It is designed for Chinese Sporttery-style markets, including win/draw/loss, handicap win/draw/loss, correct score, total goals, half/full-time, and parlays.

The Skill is built around one principle: do not confuse probability with betting value. A team can be the most likely winner and still be a poor selection if the market price is already too compressed.

## Positioning

| Dimension | Description |
|---|---|
| Use cases | World Cup previews, Sporttery market interpretation, odds sanity checks, parlay filtering |
| Primary audience | Chinese users who want disciplined football and odds analysis |
| Analysis style | Evidence first, probability-based, explicit confidence, clear risk notes |
| Output formats | Chinese chat answer, structured JSON, multi-match summary, parlay guidance |
| Safety boundary | No guaranteed profit, no loss chasing, no fabricated odds, team news, weather, or insider claims |

## Core Capabilities

| Module | Capability |
|---|---|
| Win/draw/loss | Estimates 90-minute match probabilities and explains the main drivers |
| Handicap WDL | Converts the handicap into net-goal requirements and checks margin risk |
| Correct score | Provides 2-3 score candidates while clearly labeling the market as high variance |
| Total goals | Assesses goal bands through tempo, attack quality, defensive risk, weather, and motivation |
| Half/full-time | Gives low-confidence references based on first-half caution, substitutions, and game state |
| Parlays | Keeps only stronger, lower-correlation legs and recommends skipping when evidence is thin |
| Odds value | Converts decimal odds into implied probabilities and checks market pricing |
| Risk control | Flags lineup uncertainty, injuries, weather, travel, motivation, and odds movement |

## Analysis Workflow

1. Establish match context
   Confirm the competition stage, kickoff time, venue, city, local weather, rest days, travel burden, and qualification incentives.

2. Build a pre-market football view
   Estimate probabilities from team strength, form, injuries, suspensions, tactical matchup, manager stability, motivation, venue, and weather.

3. Compare against market prices
   Convert odds into implied probabilities and separate likely outcomes from playable prices.

4. Produce market-by-market recommendations
   Cover WDL, handicap WDL, correct score, total goals, half/full-time, and parlay logic with confidence labels and risks.

5. Close with risk controls
   List missing information and variables that could break the read, such as late lineup changes, weather shifts, or unexplained odds movement.

## Installation

Copy the Skill folder into your local Codex skills directory:

```powershell
Copy-Item -Recurse .\worldcup-betting-analyst $env:USERPROFILE\.codex\skills\
```

Restart Codex, then invoke the Skill:

```text
Use $worldcup-betting-analyst to analyze France vs Brazil for all markets.

$worldcup-betting-analyst Analyze tonight's World Cup slate across WDL, handicap, score, total goals, and half/full-time.

$worldcup-betting-analyst Which two matches are most reasonable for a conservative parlay? Tell me to skip if the slate is weak.
```

## Example Output Shape

For chat usage, the Skill returns compact Chinese sections:

```text
Conclusion First
Main lean: home win is slightly preferred, but the price is not attractive enough for heavy exposure.

Match Context
- Kickoff: ...
- Venue/weather: ...
- Motivation: ...

Probability View
- Home win: 45%
- Draw: 29%
- Away win: 26%

Market Notes
- WDL: home win, medium confidence
- Handicap: watch handicap draw/loss
- Correct score: 1-0, 1-1, 2-1; high variance
- Total goals: 2 or 3 goals
- Half/full-time: draw/home or draw/draw, low confidence

Risks And Gaps
- Starting lineups unconfirmed
- Reason for odds movement unknown
- Weather may affect tempo
```

For API-ready or batch output, ask for JSON and validate the result against [`output-schema.md`](worldcup-betting-analyst/references/output-schema.md):

```powershell
python .\worldcup-betting-analyst\scripts\validate_output.py prediction.json
```

## Repository Structure

```text
worldcup-betting-analyst-skill/
├── README.md
├── LICENSE
└── worldcup-betting-analyst/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── data-sources.md
    │   ├── methodology.md
    │   └── output-schema.md
    └── scripts/
        └── validate_output.py
```

| File | Purpose |
|---|---|
| [`SKILL.md`](worldcup-betting-analyst/SKILL.md) | Core behavior rules, workflow, and safety boundaries |
| [`data-sources.md`](worldcup-betting-analyst/references/data-sources.md) | Source priority for fixtures, odds, team news, weather, and historical context |
| [`methodology.md`](worldcup-betting-analyst/references/methodology.md) | Probability discipline, odds value, confidence labels, and red flags |
| [`output-schema.md`](worldcup-betting-analyst/references/output-schema.md) | JSON contract for single-match and multi-match outputs |
| [`validate_output.py`](worldcup-betting-analyst/scripts/validate_output.py) | Validator for structured prediction files |
| [`openai.yaml`](worldcup-betting-analyst/agents/openai.yaml) | Codex/UI metadata |

## Evidence Requirements

For real or upcoming matches, the Skill should verify current information instead of relying on memory:

- official fixture, stage, kickoff time, stadium, and city;
- current Sporttery odds or user-provided market screenshots;
- injuries, suspensions, likely lineups, rotation risk, and recent form;
- local weather, humidity, wind, precipitation risk, and pitch context;
- team strength, historical context, tactics, rest, and travel.

If a field cannot be confirmed, it should be marked as `unconfirmed` and confidence should be reduced.

## Best Fit And Non-Goals

Best fit:

- structured pre-match football analysis;
- comparing probability estimates with market prices;
- identifying over-compressed favorites;
- filtering a slate into a small number of independent parlay candidates;
- producing auditable JSON prediction records.

Non-goals:

- guaranteed wins or guaranteed profit;
- loss chasing, martingale systems, borrowing, or oversized staking;
- confident recommendations without current information;
- presenting international odds as Chinese Sporttery odds;
- treating correct score as a low-risk main market.

## Risk And Responsible Use

Football outcomes are uncertain. Correct score, half/full-time, and parlay markets are especially volatile. This Skill provides analytical structure and probability estimates only. It is not financial advice and does not guarantee profit.

Responsible-use principles:

- do not chase losses;
- do not borrow money to bet;
- do not treat low odds as safety;
- do not treat parlays as risk reduction;
- use only an entertainment budget you can afford to lose.

If a user shows signs of loss chasing, emotional betting, or needing to recover losses, the Skill should stop giving picks and recommend not betting at that time.

## Inspiration And Attribution

This project is inspired by:

- [`sahuan14/worldcup-betting-analyst-skill`](https://github.com/sahuan14/worldcup-betting-analyst-skill): Sporttery workflow and risk-aware betting framing.
- [`jfjelstul/worldcup`](https://github.com/jfjelstul/worldcup): historical World Cup database structure and match context.
- [`TradingAi666/worldcup2026-prediction-skill`](https://github.com/TradingAi666/worldcup2026-prediction-skill): structured output and prediction workflow design.

This repository does not currently redistribute a bundled historical dataset. If derived data is added later, preserve the original attribution and license requirements.

## License

See [`LICENSE`](LICENSE).
