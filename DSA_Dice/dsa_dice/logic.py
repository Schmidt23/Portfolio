"""Logic utitlity for skill checks."""

import logging
from itertools import product

from dsa_dice import constants as C

logger = logging.getLogger(__name__)


def success_rate(attributes: list[int], points: int) -> float:
    """Calculate the probability of successful check without additional modifiers."""
    total = C.NUMBER_OF_ALL_POSSIBLE_ROLLS
    success = 0
    # skip calculation if any attribute value 0 -> autofail
    if any(attr <= 0 for attr in attributes):
        return 0.0
    # squash multiple for d1 in range... into itertools product
    for rolls in product(range(C.DICE_MIN, C.DICE_MAX + 1), repeat=C.NUM_ROLLS):
        # double one means critical success
        if rolls.count(C.DICE_MIN) >= C.CRIT_THRESHOLD:
            success += 1
            continue
        # double twenty means critical failure
        if rolls.count(C.DICE_MAX) >= C.CRIT_THRESHOLD:
            continue

        diff = [max(0, roll - attribute) for roll, attribute in zip(rolls, attributes)]
        if sum(diff) <= points:
            success += 1
    logger.debug(f"Number of successful checks with {points} skillpoints: {success}")
    return success / total * 100


def calculate_quality(remaining_points: int) -> int:
    """Return the quality of the skill check according to remaining points."""
    # rounds up
    qs = int((remaining_points + C.QS_DIVISOR - 1) / C.QS_DIVISOR)
    # minimum success quality=1, max possible = 6
    return max(C.QS_MIN, min(C.QS_MAX, qs))
