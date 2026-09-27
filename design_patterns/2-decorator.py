#!/usr/bin/python3
"""Module that implements the Decorator Design Pattern for beverages.
"""


class Beverage:
    """Base class for beverages."""
    def cost(self) -> int:
        """Return the cost of the beverage."""
        raise NotImplementedError

    def description(self) -> str:
        """Return the description of the beverage."""
        raise NotImplementedError


class Coffee(Beverage):
    """Concrete Coffee class."""
    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class MilkDecorator(Beverage):
    """Decorator that adds milk to a beverage."""
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Decorator that adds sugar to a beverage."""
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Decorator that adds caramel to a beverage."""
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main():
    """Main function to test the Decorator pattern."""
    beverage1 = MilkDecorator(Coffee())
    print(f"{beverage1.description()} {beverage1.cost()}")

    beverage2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{beverage2.description()} {beverage2.cost()}")

    beverage3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{beverage3.description()} {beverage3.cost()}")


if __name__ == "__main__":
    main()
