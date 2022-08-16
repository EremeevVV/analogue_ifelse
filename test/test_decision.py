from answers import Result
from traditional import decision_tree


def test_decision_tree_nonint():
    given = .01
    expected = Result.NONINT
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_positive():
    given = 4
    expected = Result.POSITIVE
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_negative():
    given = -4
    expected = Result.NEGATIVE
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_null():
    given = 0
    expected = Result.NULL
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_overhundred():
    given = 101
    expected = Result.OVERHUNDRED
    result = decision_tree(given)
    assert result == expected
