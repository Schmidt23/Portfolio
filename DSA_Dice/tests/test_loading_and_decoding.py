import json
from unittest.mock import patch

import pytest

from dsa_dice.character import load_character
from dsa_dice.skills import load_skills


def test_char_file_not_found():
    with patch("pathlib.Path.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            load_character("testchar")


def test_char_file_invalid():
    with patch(
        "dsa_dice.character.json.load",
        side_effect=json.JSONDecodeError("msg", "doc", 0),
    ):
        with pytest.raises(ValueError):
            load_character("alrik")


def test_skill_file_not_found():
    with patch("pathlib.Path.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            load_skills()


def test_skill_file_invalid():
    with patch(
        "dsa_dice.skills.json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)
    ):
        with pytest.raises(ValueError):
            load_skills()
