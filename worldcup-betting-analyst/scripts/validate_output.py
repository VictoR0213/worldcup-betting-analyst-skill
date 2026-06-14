#!/usr/bin/env python3
"""Validate JSON output produced by the worldcup-betting-analyst skill."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


CONFIDENCE_VALUES = {"high", "medium", "low", "skip"}


def fail(message: str) -> None:
    raise ValueError(message)


def require_mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{name} must be an object")
    return value


def require_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{name} must be an array")
    return value


def validate_confidence(value: Any, path: str) -> None:
    if value not in CONFIDENCE_VALUES:
        fail(f"{path} must be one of {sorted(CONFIDENCE_VALUES)}")


def validate_probabilities(match_obj: dict[str, Any], prefix: str) -> None:
    probs = require_mapping(match_obj.get("probabilities"), f"{prefix}.probabilities")
    required = ["home_win", "draw", "away_win"]
    values: list[int] = []
    for key in required:
        value = probs.get(key)
        if not isinstance(value, int):
            fail(f"{prefix}.probabilities.{key} must be an integer")
        if value < 0 or value > 100:
            fail(f"{prefix}.probabilities.{key} must be between 0 and 100")
        values.append(value)
    if sum(values) != 100:
        fail(f"{prefix}.probabilities must sum to 100")


def validate_market_object(obj: Any, path: str) -> None:
    market = require_mapping(obj, path)
    if "confidence" in market:
        validate_confidence(market["confidence"], f"{path}.confidence")


def validate_single_match(match_obj: dict[str, Any], prefix: str = "root") -> None:
    for key in ["match", "venue_weather", "probabilities", "markets", "top_pick", "risks", "information_gaps"]:
        if key not in match_obj:
            fail(f"{prefix}.{key} is required")

    validate_probabilities(match_obj, prefix)

    markets = require_mapping(match_obj["markets"], f"{prefix}.markets")
    for key in ["win_draw_loss", "handicap"]:
        validate_market_object(markets.get(key), f"{prefix}.markets.{key}")

    for key in ["correct_score", "total_goals", "half_full_time"]:
        options = require_list(markets.get(key), f"{prefix}.markets.{key}")
        if len(options) < 1:
            fail(f"{prefix}.markets.{key} must contain at least one option")
        for index, option in enumerate(options):
            validate_market_object(option, f"{prefix}.markets.{key}[{index}]")

    top_pick = require_mapping(match_obj["top_pick"], f"{prefix}.top_pick")
    rating = top_pick.get("rating")
    if not isinstance(rating, int) or rating < 0 or rating > 4:
        fail(f"{prefix}.top_pick.rating must be an integer from 0 to 4")

    require_list(match_obj["risks"], f"{prefix}.risks")
    require_list(match_obj["information_gaps"], f"{prefix}.information_gaps")


def validate_multi_match(root: dict[str, Any]) -> None:
    matches = require_list(root.get("matches"), "root.matches")
    for index, match_obj in enumerate(matches):
        validate_single_match(require_mapping(match_obj, f"root.matches[{index}]"), f"root.matches[{index}]")

    require_list(root.get("summary_table"), "root.summary_table")
    parlay = require_mapping(root.get("parlay"), "root.parlay")
    validate_confidence(parlay.get("confidence"), "root.parlay.confidence")
    require_list(parlay.get("legs"), "root.parlay.legs")


def validate(root: dict[str, Any]) -> None:
    if "matches" in root:
        validate_multi_match(root)
    else:
        validate_single_match(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.json_file.read_text(encoding="utf-8"))
        validate(require_mapping(data, "root"))
    except Exception as exc:  # noqa: BLE001 - CLI should print any validation error.
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
