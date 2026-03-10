#!/usr/bin/env python3

"""Command-line interface for performing DSA skill checks."""

import argparse
import logging
import sys

import dsa_dice.character as ch
import dsa_dice.dice as dice
import dsa_dice.logic as logic
import dsa_dice.skills as sk

logger = logging.getLogger(__name__)


def setup_logging(level: str) -> None:
    """Configure the logging system with the given log level."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )


def skill_check(
    character_data: dict[str, dict[str, int]],
    skill_defs: dict[str, list[str]],
    skill: str,
) -> str:
    """Retrieve character attributes and skill points, provides success probability, rolls dice and returns result."""
    values, skillpoints = ch.get_values(character_data, skill_defs, skill)
    probability = logic.success_rate(values, skillpoints)
    logger.info(f"Erfolgswahrscheinlichkeit: {probability}")
    rolls = dice.roll_dice()
    return dice.resolve_roll(values, rolls, skillpoints)


def main() -> None:
    """Run the CLI for performing a skill check."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="DEBUG",
    )
    parser.add_argument("-c", "--char", default="alrik")
    parser.add_argument("-s", "--skill", default="Riding")
    args = parser.parse_args()

    setup_logging(args.log_level.upper())

    char_name = args.char
    raw_skill_name = args.skill

    logger.info(f"Nutze Charakter '{char_name}' und Skill '{raw_skill_name}'")

    try:
        character_data = ch.load_character(char_name)
        skill_defs = sk.load_skills()
        skill_name = sk.normalize_skill_name(raw_skill_name, skill_defs)
        result = skill_check(character_data, skill_defs, skill_name)
        print(result)
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
