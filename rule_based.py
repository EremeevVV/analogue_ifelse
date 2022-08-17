from typing import Protocol

from data import ResultData


class RuleInterface(Protocol):

    def condition(self, val: int) -> bool:
        pass

    def action(self, val: int) -> ResultData:
        pass


class PositiveRule:

    def condition(self, val: int) -> bool:
        return val > 0

    def action(self, val: int) -> ResultData:
        if self.condition(val):
            return ResultData.POSITIVE


class NonIntRule:

    def condition(self, val: int) -> bool:
        return not isinstance(val, int)

    def action(self, val: int) -> ResultData:
        if self.condition(val):
            return ResultData.NONINT


class NullRule:

    def condition(self, val: int) -> bool:
        return val == 0

    def action(self, val: int) -> ResultData:
        if self.condition(val):
            return ResultData.NULL


class NegativeRule:

    def condition(self, val: int) -> bool:
        return val < 0

    def action(self, val: int) -> ResultData:
        if self.condition(val):
            return ResultData.NEGATIVE


class OverHundredRule:

    def condition(self, val: int) -> bool:
        return val > 100

    def action(self, val: int) -> ResultData:
        if self.condition(val):
            return ResultData.OVERHUNDRED


class RulesEvaluator:
    rules = list()

    def add_rules(self, rules: list[RuleInterface]) -> None:
        self.rules.extend(rules)

    def first_rule(self, val: int) -> ResultData:
        for rule in self.rules:
            result = rule.action(val)
            if result:
                return result


def decision_tree(val: int) -> ResultData:
    evaluator = RulesEvaluator()
    evaluator.add_rules([
        NonIntRule(),
        OverHundredRule(),
        PositiveRule(),
        NullRule(),
        NegativeRule()
    ])
    return evaluator.first_rule(val)
