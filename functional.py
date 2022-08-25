from typing import Callable
from data import ResultData, InputData


def chain_rules(struct: InputData, rules: list[Callable], default: ResultData = None) -> ResultData:
    for rule in rules:
        result = rule(struct)
        if result:
            return result


def decision_tree(struct: InputData) -> ResultData:
    fn_rule_list = [
        non_int_rule,
        positive_rules,
        null_rule,
        negative_rule
    ]
    return chain_rules(struct, fn_rule_list)


def non_int_rule(struct: InputData) -> ResultData:
    if not isinstance(struct.digit, int):
        return ResultData.NONINT


def positive_rules(struct: InputData) -> ResultData:
    positive_rule: Callable[[InputData], ResultData] = lambda x: ResultData.POSITIVE if x.digit > 0 else None
    return chain_rules(struct, [overhundred_string2_rule,
                                overhundred_rule,
                                positive_string1_rule,
                                positive_rule
                                ])


def overhundred_string2_rule(struct: InputData) -> ResultData:
    if struct.digit > 100 and struct.text == 'string2':
        return ResultData.OVERHUNDRED_STRING2


def overhundred_rule(struct: InputData) -> ResultData:
    if struct.digit > 100:
        return ResultData.OVERHUNDRED


def positive_string1_rule(struct: InputData) -> ResultData:
    if struct.digit > 0 and struct.text == 'string1':
        return ResultData.POSITIVE_STRING1


def null_rule(struct: InputData) -> ResultData:
    if struct.digit == 0:
        return ResultData.NULL


def negative_rule(struct: InputData) -> ResultData:
    if struct.digit < 0:
        return ResultData.NEGATIVE
