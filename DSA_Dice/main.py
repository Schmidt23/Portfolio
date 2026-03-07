#!/usr/bin/env python3

"""Command-line interface for performing DSA skill checks."""

import argparse
import json
import logging
import random
from functools import lru_cache
from itertools import product

logger = logging.getLogger(__name__)

CRIT_THRESHOLD = 2
DICE_MIN = 1
DICE_MAX = 20
NUM_ROLLS = 3
NUMBER_OF_ALL_POSSIBLE_ROLLS = 8000.0  # 20**3
QS_DIVISOR = 3


def setup_logging(level: str) -> None:
    """Configure the logging system with the given log level."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )


@lru_cache
def load_character(name: str) -> dict:
    """Load and cache json data from given character file."""
    try:
        with open(f"{name}.json") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Character file {name}.json not found") from e
    except json.JSONDecodeError as e:
        raise ValueError(f" {name}.json invalid") from e
    return data


@lru_cache
def load_skills() -> dict:
    """Load and cache json data from given skill file."""
    try:
        with open("skill_list.json") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError("Skill file skill_list.json not found") from e
    except json.JSONDecodeError as e:
        raise ValueError("skill file is invalid") from e
    return data


def roll_dice() -> list[int]:
    """Roll 3 D20. Return 3 random numbers between 1 and 20."""
    rolls = [random.randint(DICE_MIN, DICE_MAX) for _ in range(NUM_ROLLS)]
    return rolls


def success_rate(attributes: list[int], points: int) -> float:
    """Calculate the probability of successful check without additional modifiers."""
    total = NUMBER_OF_ALL_POSSIBLE_ROLLS
    success = 0
    # skip calculation if any attribute value 0 -> autofail
    if any(attr <= 0 for attr in attributes):
        return 0.0
    # squash multiple for d1 in range... into itertools product
    for rolls in product(random(DICE_MIN, DICE_MAX + 1), repeat=NUM_ROLLS):
        # double one means critical success
        if rolls.count(DICE_MIN) >= CRIT_THRESHOLD:
            success += 1
            continue
        # double twenty means critical failure
        if rolls.count(DICE_MAX) >= CRIT_THRESHOLD:
            continue

        diff = [max(0, roll - attribute) for roll, attribute in zip(rolls, attributes)]
        if sum(diff) <= points:
            success += 1
    logger.debug(f"Number of successful checks with {points} skillpoints: {success}")
    return success / total * 100


def get_values(
    character: dict[str, dict[str, int]], skill_list: dict[str, list[str]], skill: str
) -> tuple[list[int], int]:
    """Extract attribute values and skillpoint number for a given skill."""
    try:
        skillpoints = int(character["Skillpoints"][skill])
        skill_parts = skill_list[skill]
    except KeyError as e:
        raise KeyError(f"Skill not found: {e}") from e
    except ValueError as e:
        raise ValueError("Skill points must be integers") from e
    except TypeError as e:
        raise TypeError("Skill has invalid Type") from e

    try:
        values = [int(character["Attributes"][attr]) for attr in skill_parts]
    except KeyError as e:
        raise KeyError(f"Attribut not found: {e}") from e
    except ValueError as e:
        raise ValueError("Attributes must be integers") from e
    except TypeError as e:
        raise TypeError("Attributes has invalid Type") from e
    return values, skillpoints


def resolve_roll(
    attribute_values: list[int], rolls: list[int], skill_points: int
) -> str:
    """Compare attribute values against dice rolls and return result according to DSA 5 rules."""
    logger.debug(
        f"attribute_values={attribute_values}, rolls={rolls}, points={skill_points}"
    )

    # any value 0 or under, roll not permitted
    if any(value <= 0 for value in attribute_values):
        return "Eigenschaft 0 oder negativ. Probe nicht erlaubt"

    compare = [value - roll for value, roll in zip(attribute_values, rolls)]
    logger.debug(f"Über: {compare}")

    roll_success = all(x >= 0 for x in compare)
    logger.debug(f"Erfolgreich: {roll_success}")

    remainder = None

    if rolls.count(DICE_MIN) >= CRIT_THRESHOLD:
        return "Kritischer Erfolg"
    elif rolls.count(DICE_MAX) >= CRIT_THRESHOLD:
        return "Patzer"
    elif roll_success:
        return f"Sauber Gelungen Quali: {int((QS_DIVISOR+skill_points-1)/QS_DIVISOR)}"
    else:
        difference = [fail for fail in compare if fail < 0]
        remainder = skill_points + sum(difference)
        logger.debug(f"Punkte über: {sum(difference)}, {skill_points}")
        logger.debug(f"Rest: {remainder}")

    if remainder <= 2 and remainder >= 0:
        return f"Gelungen Quali: 1 {remainder}"
    elif remainder > 0:
        return f"Gelungen Quali: {int((QS_DIVISOR+remainder-1)/QS_DIVISOR)} {remainder}"
    else:
        return "Gescheitert"


def skill_check(
    character: dict[str, dict[str, int]], skill_list: dict[str, list[str]], skill: str
) -> str:
    """Retrieve character attributes and skill points, provides success probability, rolls dice and returns result."""
    values, skillpoints = get_values(character, skill_list, skill)
    probability = success_rate(values, skillpoints)
    logger.info(f"Erfolgswahrscheinlichkeit: {probability}")
    rolls = roll_dice()
    return resolve_roll(values, rolls, skillpoints)


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
    skill_name = args.skill

    logger.info(f"Nutze Charakter '{char_name}' und Skill '{skill_name}'")

    character = load_character(char_name)
    skills = load_skills()
    result = skill_check(character, skills, skill_name)
    print(result)


if __name__ == "__main__":
    main()
