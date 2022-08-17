from data import ResultData, InputData
from traditional import decision_tree


# from rule_based import decision_tree
# from functional import decision_tree

def test_decision_tree_nonint():
    given = InputData(0.1, 'string1')
    expected = ResultData.NONINT
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_positive():
    given = InputData(4, 'abyrvalg')
    expected = ResultData.POSITIVE
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_negative():
    given = InputData(-4, 'string1')
    expected = ResultData.NEGATIVE
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_null():
    given = InputData(0, 'string1')
    expected = ResultData.NULL
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_overhundred():
    given = InputData(101, 'abyrvalg')
    expected = ResultData.OVERHUNDRED
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_overhundred_string2():
    given = InputData(101, 'string2')
    expected = ResultData.OVERHUNDRED_STRING2
    result = decision_tree(given)
    assert result == expected


def test_decision_tree_positive_string1():
    given = InputData(10, 'string1')
    expected = ResultData.POSITIVE_STRING1
    result = decision_tree(given)
    assert result == expected
