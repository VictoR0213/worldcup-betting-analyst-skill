# World Cup Betting Analyst

Evidence-backed World Cup match analysis for Chinese Sporttery-style football markets.

[![Skill](https://img.shields.io/badge/Codex%20Skill-worldcup--betting--analyst-red)](worldcup-betting-analyst/SKILL.md)
[![Scope](https://img.shields.io/badge/Markets-胜平负%20%7C%20让球%20%7C%20比分%20%7C%20总进球%20%7C%20半全场-blue)](#what-it-covers)
[![Risk](https://img.shields.io/badge/Betting-risk--aware-black)](#disclaimer)

This repository contains a Codex Skill for disciplined World Cup football analysis. It is designed for match previews, odds sanity checks, Chinese Sporttery market interpretation, and conservative parlay construction.

The Skill separates three ideas that are often mixed together:

- what is most likely to happen on the pitch;
- whether the current odds are fairly priced;
- whether a selection belongs in a single bet, a parlay, or should be skipped.

## Latest Score Card

Snapshot: `2026-06-14`, based on current schedule context, user-provided Sporttery screenshots, and public preview data available at analysis time.

| Match | Unique Score Pick | Main Read | Risk | Official Result | Hit? | Post-Match Check |
|---|---:|---|---|---:|---|---|
| Australia vs Türkiye | `0-1` | Türkiye edge in quality; low-scoring opener | Medium | TBD | TBD | Reserve for lineup, xG, cards, weather, and game-state review |
| Germany vs Curaçao | `4-0` | Germany heavy favorite; goal-difference spot | Medium | TBD | TBD | Reserve for margin check and rotation impact |
| Netherlands vs Japan | `1-1` | Netherlands stronger, but Japan can resist the handicap | Medium | TBD | TBD | Reserve for handicap logic and late-game pressure review |
| Côte d'Ivoire vs Ecuador | `1-1` | Defensive matchup, draw has strong weight | Medium | TBD | TBD | Reserve for tempo, chance quality, and draw-read review |
| Sweden vs Tunisia | `1-0` | Sweden narrow-win profile; Tunisia can keep it tight | Medium | TBD | TBD | Reserve for first-half tempo and finishing review |

After each match, update `Official Result`, mark `Hit?` as `Yes`, `Direction`, or `No`, and use `Post-Match Check` to record whether the prediction logic was supported even when the exact score missed.

Parlay note: for Sporttery-style play, exact scores are high variance. Use score picks as a small-stake reference, not as the main staking plan. A more practical medium-risk construction is to combine safer market reads such as Netherlands `[-1]` handicap loss, Sweden win, or Côte d'Ivoire `[+1]` handicap win, depending on the live board.

## What It Covers

- 胜平负
- 让球胜平负
- 比分
- 总进球
- 半全场
- 串关 / 过关
- odds value and implied probability
- venue, weather, rest, travel, team news, and tactical context

## Install

Copy the Skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\worldcup-betting-analyst $env:USERPROFILE\.codex\skills\
```

Restart Codex, then ask questions such as:

```text
Use $worldcup-betting-analyst to analyze France vs Brazil for all markets.

$worldcup-betting-analyst 帮我看今晚世界杯胜平负、让球胜平负、比分、总进球和半全场。

$worldcup-betting-analyst 这三场怎么串更稳一点？
```

## Files

- `worldcup-betting-analyst/SKILL.md`: core workflow and behavior rules.
- `worldcup-betting-analyst/references/data-sources.md`: source hierarchy, Sporttery notes, weather and venue requirements.
- `worldcup-betting-analyst/references/methodology.md`: probability, odds, value, and confidence methodology.
- `worldcup-betting-analyst/references/output-schema.md`: JSON contract for structured outputs.
- `worldcup-betting-analyst/scripts/validate_output.py`: validator for JSON predictions.
- `worldcup-betting-analyst/agents/openai.yaml`: UI metadata.

## Method

The Skill uses a two-step workflow:

1. Build a pre-market football view from squad strength, form, availability, tactics, motivation, venue, weather, and travel.
2. Compare that view against market prices, then decide whether the pick is playable, marginal, or better skipped.

It is deliberately conservative with parlays. It avoids adding weak legs just to make a ticket look more exciting.

## Inspiration And Attribution

This Skill was inspired by:

- `sahuan14/worldcup-betting-analyst-skill`: Sporttery workflow and risk-aware betting framing.
- `jfjelstul/worldcup`: historical World Cup database structure and match context.
- `TradingAi666/worldcup2026-prediction-skill`: prompt architecture and structured output contract.

No bundled historical dataset is redistributed in this repository. If future versions include derived data from `jfjelstul/worldcup`, preserve its attribution and license requirements.

## Disclaimer

Football predictions are uncertain. This Skill does not provide guaranteed outcomes, investment advice, or a path to long-term profit. Do not chase losses, borrow money to bet, or stake money you cannot afford to lose.
