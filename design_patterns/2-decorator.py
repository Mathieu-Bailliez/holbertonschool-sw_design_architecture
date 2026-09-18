#!/usr/bin/env python3
"""Decorator pattern: add a new topping by wrapping, not by subclassing."""
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Common interface for every drink and every topping."""

    @abstractmethod
    def cost(self):
        ...

    @abstractmethod
    def description(self):
        ...


class Coffee(Beverage):
    """Base drink that the toppings wrap."""

    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    """Topping that adds milk to any beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Topping that adds sugar to any beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Topping that adds caramel to any beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    cup1 = MilkDecorator(Coffee())
    print(cup1.description(), cup1.cost())

    cup2 = MilkDecorator(SugarDecorator(Coffee()))
    print(cup2.description(), cup2.cost())

    cup3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(cup3.description(), cup3.cost())


if __name__ == "__main__":
    main()
