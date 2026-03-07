import pytest

from main import get_values


@pytest.fixture
def default_skill_list():
    return {"Riding": ["STR", "DEX", "CON"]}


@pytest.mark.parametrize(
    "skill_points, exception",
    [("abc", ValueError), (None, TypeError), ([1, 2, 3], TypeError)],
    ids=["string", "None", "List"],
)
def test_invalid_skill_points(default_skill_list, skill_points, exception):
    # arrange
    character = {
        "Skillpoints": {"Riding": skill_points},
        "Attributes": {"STR": "10", "DEX": "10", "CON": "10"},
    }
    skill_list = default_skill_list

    # act+assert
    with pytest.raises(exception):
        get_values(character, skill_list, "Riding")


@pytest.mark.parametrize(
    "attribute, exception",
    [
        ("abc", ValueError),
        (None, TypeError),
        ([1, 2, 3], TypeError),
    ],
    ids=["string", "None", "List"],
)
def test_invalid_attributes(default_skill_list, attribute, exception):
    # arrange
    character = {
        "Skillpoints": {"Riding": "5"},
        "Attributes": {"STR": attribute, "DEX": "10", "CON": "10"},
    }
    skill_list = default_skill_list

    # act+assert
    with pytest.raises(exception):
        get_values(character, skill_list, "Riding")


def test_attribute_key(default_skill_list):
    # arrange
    character = {
        "Skillpoints": {"Riding": "5"},
        "Attributes": {"non_existant": "10", "DEX": "10", "CON": "10"},
    }
    skill_list = default_skill_list

    # act+assert
    with pytest.raises(KeyError):
        get_values(character, skill_list, "Riding")


def test_skill_key(default_skill_list):
    # arrange
    character = {
        "Skillpoints": {"non_existant": "5"},
        "Attributes": {"STR": "10", "DEX": "10", "CON": "10"},
    }
    skill_list = default_skill_list

    # act+assert
    with pytest.raises(KeyError):
        get_values(character, skill_list, "Riding")


def test_return_successful(default_skill_list):
    # arrange
    character = {
        "Skillpoints": {"Riding": "5"},
        "Attributes": {"STR": "10", "DEX": "10", "CON": "10"},
    }
    skill_list = default_skill_list

    result = get_values(character, skill_list, "Riding")

    assert result == ([10, 10, 10], 5)
