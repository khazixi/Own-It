import dataclasses
import abc_rentals

from typing import Type, NamedTuple

"""
All the data for propertiesis listed here. and constructor methods are listed
"""

Rental = Type('Rental', bound='BaseRental')


@dataclasses.dataclass
class Building(abc_rentals.BaseRental):
    """
    Represents the data of all the properties and effect spots on the board
    """

    color: str
    house_price: int
    # NOTE: if hotel has a value then house must be 0
    house: int = dataclasses.field(init=False, default=0)
    # NOTE: If house has a value hotel must be 0
    hotel: int = dataclasses.field(init=False, default=0)

    @classmethod
    def from_json(cls: Rental, data: dict, color: str, name: str) -> Rental:
        data_slice = data["Building"][color][name]
        return cls(name, "Building", data_slice['position'],
                   data_slice['rent'], data_slice['price'],
                   color, data_slice['house_price'])


@dataclasses.dataclass
class Utility(abc_rentals.BaseRental):
    @classmethod
    def from_json(cls: Rental, data: dict, name: str) -> Rental:
        data_slice = data["Utility"][name]
        return cls(name, "Utility", data_slice['position'],
                   data_slice['rent'], data_slice['price'])


@dataclasses.dataclass
class Railroad(abc_rentals.BaseRental):
    @classmethod
    def from_json(cls: Rental, data: dict, name: str) -> Rental:
        data_slice = data["Railroad"][name]
        return cls(name, "Railroad", data_slice['position'],
                   data_slice['rent'], data_slice['price'])


class Tax(NamedTuple):
    name: str
    position: int
    tax: int


class Chance(NamedTuple):
    position: int
    name: str = "Chance"


class Community_Chest(NamedTuple):
    position: int
    name: str = "Community Chest"
