from typing import List, Tuple

from game.die import Die


class Player:
    def __init__(self, color:Tuple[int,int,int], dice: List[Die]) -> None:
        self.checker_color = color
        self.score = 0
        self.dice: List[Die] = dice
        self.ready_to_bear_off: bool = False

    def roll_dice(self):
        for die in self.dice:
            die.roll()