# worldcup-betting-analyst

A Codex Skill for evidence-backed World Cup football match and竞彩-style market analysis.

It covers:

- 胜平负
- 让球胜平负
- 比分
- 总进球
- 半全场
- 串关/过关

The Skill is designed for analysis and entertainment-oriented decision support. It separates match probability from odds value, checks venue/weather and live team news, and recommends skipping matches when evidence or price is poor.

## Install

Copy the Skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\worldcup-betting-analyst $env:USERPROFILE\.codex\skills\
```

Then ask Codex questions such as:

```text
Use $worldcup-betting-analyst to analyze France vs Brazil for all markets.
今晚世界杯比赛帮我挑一个 2 串 1。
这场让球胜平负和总进球怎么选？
```

## Files

- `worldcup-betting-analyst/SKILL.md`: core workflow and behavior rules.
- `worldcup-betting-analyst/references/data-sources.md`: source hierarchy, Sporttery notes, weather/venue requirements.
- `worldcup-betting-analyst/references/methodology.md`: probability, odds, value, and confidence methodology.
- `worldcup-betting-analyst/references/output-schema.md`: JSON contract for structured outputs.
- `worldcup-betting-analyst/scripts/validate_output.py`: validator for JSON predictions.
- `worldcup-betting-analyst/agents/openai.yaml`: UI metadata.

## Inspiration And Attribution

This Skill was inspired by:

- `sahuan14/worldcup-betting-analyst-skill`:竞彩 workflow and risk-aware betting framing.
- `jfjelstul/worldcup`: historical World Cup database structure and match context.
- `TradingAi666/worldcup2026-prediction-skill`: prompt architecture and structured output contract.

No bundled historical dataset is redistributed in this repository. If future versions include derived data from `jfjelstul/worldcup`, preserve its attribution and license requirements.

## Disclaimer

Football predictions are uncertain. This Skill does not provide guaranteed outcomes, investment advice, or a path to long-term profit. Do not chase losses, borrow money to bet, or stake money you cannot afford to lose.
