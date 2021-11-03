import pygame

from game.constants import COLOR_ONE, COLOR_TWO
from .board import Board
from .player import Player
from .point import Point

class Game:
    def __init__(self, win:pygame.Surface):
        self.win:pygame.Surface = win
        self._init()
        self.board:Board = Board(win)
    
    def select(self, point_num: int):
        if self.selected:
            if point_num + 1 in self.board.legal_moves:
                pass

    def update(self):
        pygame.display.update()
    
    def reset(self):
        self._init()

    def _init(self):
        self.selected:Point = None
        self.player_one:Player = Player(COLOR_ONE)
        self.player_two:Player = Player(COLOR_TWO)
        self.board: Board = None
        self.turn:Player = None