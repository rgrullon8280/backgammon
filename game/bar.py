from typing import List, Tuple

from game.player import Player
from .constants import BAR_WIDTH, WIDTH, HEIGHT, COLOR_ONE, COLOR_TWO
from .checker import Checker

class Bar:
    def __init__(self):
        self.checkers: dict[Tuple[int,int,int],List[Checker]] = {
            COLOR_ONE: [],
            COLOR_TWO: []
        }
    

    def has_checkers_on_bar(self, player: Player) -> bool:
        return len(self.checkers[player.checker_color]) > 0
