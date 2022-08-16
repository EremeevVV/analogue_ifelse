from answers import Result


def decision_tree(val: int) -> Result:
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


def non_int_rule(val: int) -> Result:
    if not isinstance(val, int):
        return Result.NONINT


def overhundred_rule(val: int) -> Result:
    if val > 100:
        return Result.OVERHUNDRED


def positive_rule(val: int) -> Result:
    if val > 0:
        return Result.POSITIVE


def null_rule(val: int) -> Result:
    if val == 0:
        return Result.NULL


def negative_rule(val: int) -> Result:
    if val < 0:
        return Result.NEGATIVE
