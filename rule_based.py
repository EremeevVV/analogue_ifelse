from typing import Protocol

from answers import Result


class RuleInterface(Protocol):

    def condition(self, val: int) -> bool:
        pass

    def action(self, val: int) -> Result:
        pass


class PositiveRule:

    def condition(self, val: int) -> bool:
        return val > 0

    def action(self, val: int) -> Result:
        if self.condition(val):
            return Result.POSITIVE


class NonIntRule:

    def condition(self, val: int) -> bool:
        return not isinstance(val, int)

    def action(self, val: int) -> Result:
        if self.condition(val):
            return Result.NONINT


class NullRule:

    def condition(self, val: int) -> bool:
        return val == 0

    def action(self, val: int) -> Result:
        if self.condition(val):
            return Result.NULL


class NegativeRule:

    def condition(self, val: int) -> bool:
        return val < 0

    def action(self, val: int) -> Result:
        if self.condition(val):
            return Result.NEGATIVE


class OverHundredRule:

    def condition(self, val: int) -> bool:
        return val > 100

    def action(self, val: int) -> Result:
        if self.condition(val):
            return Result.OVERHUNDRED


class RulesEvaluator:
    rules = list()

    def add_rules(self, rules: list[RuleInterface]) -> None:
        self.rules.extend(rules)

    def first_rule(self, val: int) -> Result:
        for rule in self.rules:
            result = rule.action(val)
            if result:
                return result


def decision_tree(val: int) -> Result:
    evaluator = RulesEvaluator()
    evaluator.add_rules([
        NonIntRule(),
        OverHundredRule(),
        PositiveRule(),
        NullRule(),
        NegativeRule()
    ])
    return evaluator.first_rule(val)
