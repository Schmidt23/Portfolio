import pytest

from dsa_dice.logic import success_rate


@pytest.mark.parametrize(
    "vals",
    [
        [0, 20, 20],
        [20, 20, 0],
        [20, 0, 20],
        [0, 0, 0],
        [20, 20, -3],
    ],
    ids=["0,20,20", "20,20,0", "20,0,20", "0,0,0", "20,20,-3"],
)
def test_autofail(vals):
    skill_points = 20

    result = success_rate(vals, skill_points)

    assert result == 0.0


def test_only_crits():
    attribute_values = [1, 1, 1]
    skill_points = 0

    # only crits can succeed
    # (1,1,n) -> 19 combinations (1,n,1) -> 19 ... -> 57 + (1,1,1) = 58
    expected = 58 / 8000 * 100

    assert success_rate(attribute_values, skill_points) == expected


def test_crit_fail_chance():
    attribute_values = [20, 20, 20]
    skill_points = 100

    # only crit fail can fail
    expected = (8000 - 58) / 8000 * 100

    assert success_rate(attribute_values, skill_points) == expected


def test_success_rate_is_deterministic():
    attribute_values = [13, 14, 10]
    skill_points = 6

    result = success_rate(attribute_values, skill_points)

    assert result == success_rate(attribute_values, skill_points)
