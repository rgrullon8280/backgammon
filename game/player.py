from typing import List, Tuple

from game.die import Die


class Player:
    def __init__(self, color:Tuple[int,int,int], dice: List[Die], direction:int) -> None:
        self.checker_color = color
        self.score = 0
        self.dice: List[Die] = dice
        self.ready_to_bear_off: bool = False
        self.has_checkers_on_bar: bool = False
        self.direction:int = direction

    def roll_dice(self):
        for die in self.dice:
            die.roll()