# Output Schema

Use this schema when the user asks for JSON, API-ready output, or batch predictions. For normal chat, the same fields can be rendered as readable Chinese sections.

## Single Match JSON

```json
{
  "generated_at": "2026-06-14T12:00:00+08:00",
  "timezone": "Asia/Shanghai",
  "match": {
    "competition": "FIFA World Cup 2026",
    "stage": "Group stage",
    "home_team": "Team A",
    "away_team": "Team B",
    "kickoff_beijing": "2026-06-20T03:00:00+08:00",
    "kickoff_local": "2026-06-19T15:00:00-04:00",
    "stadium": "Stadium Name",
    "city": "City",
    "country": "Country"
  },
  "venue_weather": {
    "temperature_c": 26,
    "humidity_pct": 62,
    "wind_kph": 14,
    "precipitation": "low",
    "altitude_m": 30,
    "impact": "neutral"
  },
  "probabilities": {
    "home_win": 45,
    "draw": 28,
    "away_win": 27
  },
  "markets": {
    "win_draw_loss": {
      "selection": "home_win",
      "odds": 2.1,
      "confidence": "medium",
      "single_allowed": true,
      "reason": "Short reason"
    },
    "handicap": {
      "line": "-1",
      "selection": "handicap_draw",
      "odds": 3.4,
      "confidence": "low",
      "single_allowed": false,
      "reason": "Short reason"
    },
    "correct_score": [
      {"score": "1-0", "confidence": "low", "reason": "Short reason"},
      {"score": "1-1", "confidence": "low", "reason": "Short reason"}
    ],
    "total_goals": [
      {"selection": "2 goals", "confidence": "medium", "reason": "Short reason"},
      {"selection": "3 goals", "confidence": "medium", "reason": "Short reason"}
    ],
    "half_full_time": [
      {"selection": "draw/home", "confidence": "low", "reason": "Short reason"},
      {"selection": "draw/draw", "confidence": "low", "reason": "Short reason"}
    ]
  },
  "top_pick": {
    "play": "win_draw_loss",
    "selection": "home_win",
    "odds": 2.1,
    "rating": 3,
    "action": "play_small"
  },
  "risks": [
    "Key risk 1",
    "Key risk 2"
  ],
  "information_gaps": [
    "Unconfirmed lineup"
  ],
  "responsible_note": "Predictions are uncertain; do not chase losses or stake money you cannot afford to lose."
}
```

Rules:

- `probabilities.home_win + probabilities.draw + probabilities.away_win` must equal 100.
- `confidence` must be one of `high`, `medium`, `low`, `skip`.
- `rating` is an integer 0-4:
  - 0 = skip
  - 1 = entertainment only
  - 2 = weak lean
  - 3 = playable
  - 4 = strongest relative lean, still not guaranteed
- Use `null` for unavailable odds, not fabricated numbers.
- Use `single_allowed: null` when single/parlay status cannot be verified.

## Multi Match JSON

```json
{
  "generated_at": "2026-06-14T12:00:00+08:00",
  "timezone": "Asia/Shanghai",
  "matches": [],
  "summary_table": [
    {
      "match": "Team A vs Team B",
      "kickoff_beijing": "2026-06-20T03:00:00+08:00",
      "top_pick": "home_win",
      "odds": 2.1,
      "rating": 3,
      "one_line_reason": "Short reason"
    }
  ],
  "parlay": {
    "recommendation": "2x1",
    "legs": [
      {"match": "Team A vs Team B", "play": "win_draw_loss", "selection": "home_win", "odds": 2.1},
      {"match": "Team C vs Team D", "play": "total_goals", "selection": "2 or 3 goals", "odds": 1.9}
    ],
    "combined_odds": 3.99,
    "confidence": "medium",
    "risk_note": "Parlay risk multiplies; skip if any lineup news turns negative."
  }
}
```

If there are fewer than two playable legs, set:

```json
"parlay": {
  "recommendation": "skip",
  "legs": [],
  "combined_odds": null,
  "confidence": "skip",
  "risk_note": "Not enough high-quality independent legs."
}
```
