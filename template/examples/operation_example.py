import operator
from abc import ABCMeta, abstractmethod


class Operator(metaclass=ABCMeta):
    def __init__(self):
        self.result = None

    @abstractmethod
    def operation(self):
        pass

    def operate(self, a, b):
        op = self.operation()
        self.result = op(a, b)

    def get_result(self):
        return self.result


class Sum(Operator):
    def operation(self):
        return operator.add


class Sub(Operator):
    def operation(self):
        return operator.sub


class Mult(Operator):
    def operation(self):
        return operator.mul


class Div(Operator):
    def operation(self):
        return operator.truediv


class Calculator:

    def __init__(self):
        self.op = None

    @staticmethod
    def calc(a, b, op):
        op = op()
        op.operate(a, b)
        return op.get_result()


def test_operations():
    # Operator
    sm = Sum()
    sb = Sub()
    mt = Mult()
    dv = Div()

    # Tests
    sm.operate(5, 6)
    assert sm.get_result() == 11

    sb.operate(5, 6)
    assert sb.get_result() == -1

    mt.operate(5, 6)
    assert mt.get_result() == 30

    dv.operate(5, 6)
    assert dv.get_result() == 5 / 6


def test_calculator():
    # Calculator
    calculator = Calculator()

    # Tests
    assert calculator.calc(a=10, b=10, op=Sum) == 20
    assert calculator.calc(a=10, b=10, op=Sub) == 0
    assert calculator.calc(a=10, b=10, op=Mult) == 100
    assert calculator.calc(a=10, b=10, op=Div) == 1


if __name__ == '__main__':
    test_operations()
    test_calculator()
