import pytest

from dsa_dice.dice import resolve_roll


@pytest.fixture
def default_vals():
    return [10, 10, 10]


@pytest.mark.parametrize(
    "rolls",
    [
        [1, 1, 20],
        [1, 20, 1],
        [20, 1, 1],
        [1, 1, 1],
    ],
    ids=["1,1,20", "1,20,1", "20,1,1", "1,1,1"],
)
def test_crit_success(default_vals, rolls):
    # arrange
    vals = default_vals
    points = 5

    # act
    result = resolve_roll(vals, rolls, points)

    # assert
    assert result == "Kritischer Erfolg"


@pytest.mark.parametrize(
    "rolls",
    [
        [1, 20, 20],
        [20, 20, 1],
        [20, 1, 20],
        [20, 20, 20],
    ],
    ids=["1,20,20", "20,20,1", "20,1,20", "20,20,20"],
)
def test_crit_fail(default_vals, rolls):
    # arrange
    vals = default_vals
    points = 25

    # act
    result = resolve_roll(vals, rolls, points)

    # assert
    assert result == "Patzer"


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
def test_impossible_roll(vals):
    # arrange
    rolls = [1, 1, 1]
    points = 25

    # act
    result = resolve_roll(vals, rolls, points)

    # assert
    assert result == "Eigenschaft 0 oder negativ. Probe nicht erlaubt"


@pytest.mark.parametrize(
    "points, expected",
    [(1, 1), (3, 1), (2, 1), (0, 1), (50, 6)],
    ids=["1", "3", "2", "0", "50"],
)
def test_success_quality(default_vals, points, expected):
    # arrange
    vals = default_vals
    rolls = [9, 9, 9]

    # act
    result = resolve_roll(vals, rolls, points)

    # assert
    assert result == f"Sauber Gelungen Quali: {expected}"


@pytest.mark.parametrize(
    "points",
    [
        3,
        4,
        5,
        6,
    ],
    ids=["3", "4", "5", "6"],
)
def test_success_quality_one(default_vals, points):
    # arrange
    vals = default_vals
    rolls = [11, 11, 11]

    # act
    result = resolve_roll(vals, rolls, points)

    # assert
    assert result == f"Gelungen Quali: 1 {points-3}"


@pytest.mark.parametrize(
    "points, expected",
    [(4, 1), (7, 2), (10, 3), (13, 4), (16, 5), (19, 6)],
    ids=["4", "7", "10", "13", "16", "19"],
)
def test_success_quality_edge_cases(default_vals, points, expected):
    # arrange
    vals = default_vals
    rolls = [11, 11, 11]

    # act
    result = resolve_roll(vals, rolls, points)

    # assert
    assert result == f"Gelungen Quali: {expected} {points-3}"
