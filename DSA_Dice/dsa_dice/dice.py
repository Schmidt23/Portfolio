"""Roll dice and resolve the roll according to DSA 5 rules."""

import logging
import random

import dsa_dice.logic as logic
from dsa_dice import constants as C

logger = logging.getLogger(__name__)


def roll_dice() -> list[int]:
    """Roll 3 D20. Return 3 random numbers between 1 and 20."""
    rolls = [random.randint(C.DICE_MIN, C.DICE_MAX) for _ in range(C.NUM_ROLLS)]
    return rolls


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

    if rolls.count(C.DICE_MIN) >= C.CRIT_THRESHOLD:
        return "Kritischer Erfolg"
    elif rolls.count(C.DICE_MAX) >= C.CRIT_THRESHOLD:
        return "Patzer"
    elif roll_success:
        qs = logic.calculate_quality(skill_points)
        return f"Sauber Gelungen Quali: {qs}"
    else:
        difference = [fail for fail in compare if fail < 0]
        remainder = skill_points + sum(difference)
        logger.debug(f"Punkte über: {sum(difference)}, {skill_points}")
        logger.debug(f"Rest: {remainder}")

    if remainder >= 0:
        qs = logic.calculate_quality(remainder)
        return f"Gelungen Quali: {qs} {remainder}"
    else:
        return "Gescheitert"
