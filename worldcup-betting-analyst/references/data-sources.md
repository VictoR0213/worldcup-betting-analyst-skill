# Data Sources

Use live, source-backed data whenever analyzing a real or upcoming match. Date-sensitive football information changes quickly; stale facts are a major failure mode.

## Source Priority

1. Official or primary sources
   - FIFA match center, tournament schedule, official squad lists, disciplinary reports.
   - National-team federation announcements.
   - Stadium or event pages for venue details.
   - Official meteorological services when available.

2. Market data
   - China Sporttery/竞彩 pages or JSON endpoints when accessible and lawful to query.
   - Major international odds screens only as comparison data, not as a replacement for竞彩 prices.
   - Record the capture time and timezone.

3. Team news
   - Reuters, AP, BBC Sport, ESPN, The Athletic, local federation releases, verified journalist reports.
   - Avoid unsourced social media claims unless clearly labeled as unverified.

4. Historical database
   - `jfjelstul/worldcup` is useful for historical World Cup matches, stadiums, teams, goals, appearances, and event records.
   - Use it for context, not as a live 2026 source unless the repository has been updated and verified.
   - Attribution: Joshua C. Fjelstul, Ph.D., The Fjelstul World Cup Database, https://github.com/jfjelstul/worldcup.

## Sporttery / 竞彩 Notes

When available, prefer structured JSON over scraping rendered pages.

Typical Chinese竞彩 football markets:

- `had`: 胜平负, home/draw/away.
- `hhad`: 让球胜平负, with an integer goal line.
- `crs`: correct score.
- `ttg`: total goals, usually 0, 1, 2, 3, 4, 5, 6, 7+.
- `hafu`: half/full-time, 9 combinations.

If the response includes a single/过关 field, use it to determine whether a market supports single-match betting. If this cannot be confirmed, state that the user must verify in the official app or sales channel.

Do not invent竞彩 odds. If only international odds are available, clearly label them as non-竞彩 comparison odds.

## Weather And Venue

For the venue:

- Confirm stadium, city, country, kickoff local time, and altitude if material.
- For short-term forecasts, collect temperature, humidity, wind speed, precipitation probability, and severe-weather notes.
- For long-range matches where forecasts are unavailable, use historical climate normals only as weak background and mark lower confidence.

Weather interpretation:

- Heat and high humidity can lower pressing intensity and second-half pace.
- Strong wind can reduce crossing, long passing, and set-piece precision.
- Heavy rain can increase randomness, defensive errors, and under/over uncertainty depending on pitch drainage.
- Altitude can matter for teams not acclimatized.

## License And Attribution

The referenced repositories are inspiration and source material, not text to copy wholesale:

- `sahuan14/worldcup-betting-analyst-skill`: betting-analysis workflow and竞彩 framing.
- `jfjelstul/worldcup`: historical World Cup database; respect its license and attribution requirements if data is redistributed.
- `TradingAi666/worldcup2026-prediction-skill`: prompt architecture, output contract idea, and daily intelligence slot.

If bundling derived datasets from CC-BY-SA sources later, preserve attribution and compatible licensing.
