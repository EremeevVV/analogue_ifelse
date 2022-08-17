from data import ResultData


def decision_tree(val: int) -> ResultData:
    fn_rule_list = [
        non_int_rule,
        overhundred_rule,
        positive_rule,
        null_rule,
        negative_rule
    ]
    for rule in fn_rule_list:
        result = rule(val)
        if result:
            return result


def non_int_rule(val: int) -> ResultData:
    if not isinstance(val, int):
        return ResultData.NONINT


def overhundred_rule(val: int) -> ResultData:
    if val > 100:
        return ResultData.OVERHUNDRED


def positive_rule(val: int) -> ResultData:
    if val > 0:
        return ResultData.POSITIVE


def null_rule(val: int) -> ResultData:
    if val == 0:
        return ResultData.NULL


def negative_rule(val: int) -> ResultData:
    if val < 0:
        return ResultData.NEGATIVE
