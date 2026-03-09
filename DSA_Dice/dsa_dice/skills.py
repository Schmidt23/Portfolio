"""Load skill list from the data folder and normalize the skill name."""

import json
import logging
from functools import lru_cache

from dsa_dice import constants as C

logger = logging.getLogger(__name__)


@lru_cache
def load_skills() -> dict:
    """Load and cache json data from given skill file."""
    file_path = C.BASE_DIR / "skill_list.json"
    try:
        with file_path.open("r") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Skill file {file_path} not found") from e
    except json.JSONDecodeError as e:
        raise ValueError("skill file is invalid") from e
    logger.debug(f"Loaded {len(data)} skills from {file_path}")
    return data


def normalize_skill_name(skill_input: str, skills: dict) -> str:
    """Normalize user input to match case-sensitive skill-key."""
    skill_input_lower = skill_input.lower()
    skill_map = {key.lower(): key for key in skills.keys()}

    if skill_input_lower not in skill_map:
        raise ValueError(f"Skill {skill_input} does not exist")

    normalized = skill_map[skill_input_lower]

    logger.debug(f"Normalized skill '{skill_input}' -> '{normalized}'")
    return normalized
