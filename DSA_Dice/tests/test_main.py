import pytest

from dsa_dice.main import main

VALID_RESULTS = ["Gelungen", "Sauber", "Patzer", "Kritischer", "Gescheitert"]


@pytest.fixture
def default_vals():
    return [10, 10, 10]


def test_cli_short(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["prog", "-c", "alrik", "-s", "Riding"])

    main()

    out = capsys.readouterr().out
    print(f"CLI Output: {out}")
    assert any(word in out for word in VALID_RESULTS), f"Output war:\n{out!r}"


def test_cli_long(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["prog", "--char", "alrik", "--skill", "Riding"])

    main()

    out = capsys.readouterr().out
    print(f"CLI Output: {out}")
    assert any(word in out for word in VALID_RESULTS), f"Output war:\n{out!r}"


def test_cli_error_character(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["prog", "--char", "unknown", "--skill", "Riding"])

    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 1


def test_cli_error_skill(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["prog", "--char", "alrik", "--skill", "Ryeding"])

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 1


def test_cli_error_loglevel(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv", ["prog", "--char", "alrik", "--skill", "Riding", "-l", "STUFF"]
    )

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 2
    out = capsys.readouterr()
    assert "invalid" in out.err
