import random

import rentals
import helper


class Dice:
    def roll(self) -> int:
        return random.randint(1, 6)


class Board:
    def __init__(self) -> None:
        self.rental_map: dict[int, rentals.Rental] = {}
        self.player_list: list[helper.Owner] = []
