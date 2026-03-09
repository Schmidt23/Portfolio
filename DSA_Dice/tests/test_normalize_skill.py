import pytest

from dsa_dice.skills import normalize_skill_name


@pytest.mark.parametrize(
    "skill",
    ["RIDING", "RIding", "riding", "riDinG"],
    ids=["RIDING", "RIding", "riding", "riDinG"],
)
def test_cli_skill_normalization(skill):
    skills = {"Riding": [], "Swimming": []}

    normalized = normalize_skill_name(skill, skills)

    assert normalized == "Riding"
