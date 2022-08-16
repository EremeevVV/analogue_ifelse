from answers import Result


def decision_tree(val: int) -> Result:
    if not isinstance(val, int):
        return Result.NONINT
    if val > 0:
        if val > 100:
            return Result.OVERHUNDRED
        return Result.POSITIVE
    elif val == 0:
        return Result.NULL
    else:
        return Result.NEGATIVE
