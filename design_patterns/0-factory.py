#!/usr/bin/env python3
"""Factory pattern: extend a vehicle registry without modifying create()."""
from __future__ import annotations


class Bus:
    """Vehicle that travels on the road."""

    def mode(self) -> str:
        return "road"


class Train:
    """Vehicle that travels on rails."""

    def mode(self) -> str:
        return "rails"


class Bike:
    """Vehicle that travels in a bike lane."""

    def mode(self) -> str:
        return "lane"


class Scooter:
    """Vehicle that travels in a scooter lane."""

    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    """Create vehicles by name using a registry of kinds to classes."""

    def __init__(self) -> None:
        self._registry: dict[str, type] = {
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        }

    def register_kind(self, name: str, cls: type) -> None:
        self._registry[name] = cls

    def create(self, kind: str) -> object:
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind!r}")
        return self._registry[kind]()


def main() -> None:
    factory = VehicleFactory()

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
