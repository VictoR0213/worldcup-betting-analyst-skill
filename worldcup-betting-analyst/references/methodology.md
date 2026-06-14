# Methodology

The method has two separate stages:

1. Estimate football probabilities before looking too closely at the odds.
2. Compare those probabilities with market prices to decide whether any selection is playable.

Never collapse these into "team likely wins, therefore buy it."

## Factor Model

Use a flexible weighting system; adjust by stage and data quality.

Baseline weights for World Cup matches:

| Factor | Typical Weight | What To Consider |
|---|---:|---|
| Team strength | 25% | Elo/FIFA rank, squad value, club level, depth, manager stability |
| Recent form | 20% | Last 5-10 matches, opponent quality, xG/xGA if available |
| Squad availability | 15% | injuries, suspensions, likely XI, goalkeeper and striker availability |
| Tactical matchup | 15% | pressing resistance, transition defense, set pieces, wide areas |
| Motivation and stage | 10% | group incentives, knockout caution, qualification math |
| Venue/weather/travel | 10% | host advantage, climate, altitude, rest, travel distance |
| Market sanity check | 5% | odds movement, market disagreement, public overreaction |

Adjustments:

- Knockout match: raise draw/low-score probability unless both teams are structurally open.
- Final group match: motivation and goal-difference incentives can dominate baseline strength.
- Host nation: add context but do not overstate it; estimate crowd/travel/referee-pressure effects separately.
- Extreme weather: lower confidence and widen score distribution.

## Probability Discipline

For 胜平负:

- Produce probabilities as integers summing to 100.
- Avoid >75% for a team unless the mismatch is very strong and verified.
- Treat 90-minute draw explicitly in knockout matches.
- If market and your view differ heavily, first suspect missing information before calling it value.

For goals:

- A simple Poisson-style mental model is acceptable:
  - Estimate expected goals for each team.
  - Convert to likely score bands.
  - Stress-test against lineup, weather, motivation, and pace.
- Do not overfit exact score. Correct score is high variance.

For handicap:

- Translate the handicap into net-goal requirements.
- Check whether the favorite's game state supports pushing for margin.
- In group play, a team may stop attacking after a narrow lead; in goal-difference scenarios, the opposite may be true.

For half/full-time:

- Consider first-half caution, substitution patterns, stamina, and tactical adjustment.
- Avoid high confidence unless the teams' first-half tendencies are well supported.

## Odds And Value

Use decimal odds.

- Implied probability = `1 / odds`.
- Overround = sum of implied probabilities - 100%.
- De-vigged probability = each implied probability divided by the implied-probability sum.
- Rough expected value = `your_probability * odds - 1`.

Interpretation:

- Positive EV is rare in high-margin markets.
- Low odds are not "safe"; they are the price of a high-probability event.
- A favorite can be the most likely winner and still be a bad price.
- Parlays multiply both risk and margin.

## Confidence Labels

Use these labels consistently:

| Label | Meaning |
|---|---|
| high | Strong evidence, market not obviously over-compressed, limited missing data |
| medium | Reasonable read but some uncertainty or price concern |
| low | High variance, missing data, poor price, or entertainment-only market |
| skip | No playable edge or too much uncertainty |

Correct score should almost never exceed `low` or `medium-low` confidence.

## Red Flags

Recommend skip or reduce confidence when:

- Key lineup news is unavailable close to kickoff.
- Weather is severe or forecast confidence is low.
- Odds moved sharply and the reason is unknown.
- The user is trying to force a parlay from weak matches.
- The market price is far worse than the estimated probability justifies.
- The match has unclear motivation or likely heavy rotation.
