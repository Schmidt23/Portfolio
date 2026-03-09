"""Character loading utilities for the DSA dice CLI.

This module provides functions to load and cache character JSON files
from the project's data directory. It resolves file paths relative to
the package structure  and raises errors when files
are missing or invalid.

"""

import json
import logging
from functools import lru_cache

from dsa_dice import constants as C

logger = logging.getLogger(__name__)


@lru_cache
def load_character(name: str) -> dict:
    """Load and cache json data from given character file."""
    file_path = C.BASE_DIR / f"{name}.json"
    try:
        with file_path.open("r") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Character file {name}.json not found") from e
    except json.JSONDecodeError as e:
        raise ValueError(f" {name}.json invalid") from e
    return data


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
