#!/usr/bin/python3
"""Module that implements the Factory Design Pattern with a registry.
"""


class Vehicle:
    """Base class for all vehicles."""
    def mode(self):
        """Return the movement mode of the vehicle."""
        raise NotImplementedError


class Bus(Vehicle):
    """Bus concrete class."""
    def mode(self):
        return "road"


class Train(Vehicle):
    """Train concrete class."""
    def mode(self):
        return "rails"


class Bike(Vehicle):
    """Bike concrete class."""
    def mode(self):
        return "lane"


class Scooter(Vehicle):
    """Scooter concrete class."""
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    """A registry-based factory for creating vehicles."""
    def __init__(self):
        self._registry = {}

    def register_kind(self, kind: str, cls):
        """Register a new vehicle class with a string key."""
        self._registry[kind] = cls

    def create(self, kind: str):
        """Create and return an instance of the requested vehicle kind."""
        cls = self._registry.get(kind)
        if not cls:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return cls()


def main():
    """Main function to test the VehicleFactory."""
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
