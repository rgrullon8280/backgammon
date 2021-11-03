import pygame

from game.constants import COLOR_ONE, COLOR_TWO
from game.die import Die
from .board import Board
from .player import Player
from .point import Point

class Game:
    def __init__(self, win:pygame.Surface):
        self.win:pygame.Surface = win
        self._init()
    
    def select(self, point_num:int):
        if point_num is None:
            return
        point:Point = self.board.points[point_num]
        if self.selected:
            if point in self.board.legal_moves:
                self.board.move_checker(self.selected, point)
                self.next_turn()
        else:
            if point.checker_color == self.turn.checker_color:
                self.selected = point
                self.board.calc_legal_moves(self.turn,self.selected)

    def next_turn(self):
        if self.turn == self.player_one:
            self.turn = self.player_two
        else:
            self.turn = self.player_one
        

    def update(self):
        pygame.display.update()
    
    def reset(self):
        self._init()
    
    def start_roll(self) -> Player:
        while self.player_one.dice[0].number != self.player_two.dice[0].number:
            self.player_one.roll_dice()
            self.player_two.roll_dice()

        die_one_value = self.player_one.dice[0].number
        die_two_value = self.player_two.dice[0].number
        return self.player_one if die_one_value > die_two_value else self.player_two


    def _init(self):
        self.selected:Point = None
        self.player_one:Player = Player(COLOR_ONE,[Die(),Die()])
        self.player_two:Player = Player(COLOR_TWO,[Die(),Die()])
        self.board:Board = Board(self.win)
        self.board.draw_dice(self.player_one,self.player_two)
        self.turn:Player = self.start_roll()