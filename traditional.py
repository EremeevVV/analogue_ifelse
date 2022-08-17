from data import ResultData, InputData


def decision_tree(struct: InputData) -> ResultData:
    if not isinstance(struct.digit, int):
        return ResultData.NONINT
    if struct.digit > 0:
        if struct.digit > 100:
            if struct.text == 'string2':
                return ResultData.OVERHUNDRED_STRING2
            return ResultData.OVERHUNDRED
        if struct.text == 'string1':
            return ResultData.POSITIVE_STRING1
        return ResultData.POSITIVE
    elif struct.digit == 0:
        return ResultData.NULL
    else:
        return ResultData.NEGATIVE
