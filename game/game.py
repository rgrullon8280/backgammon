from typing import List, Tuple
import pygame
from game.Destination import Destination

from game.constants import COLOR_ONE, COLOR_TWO
from game.die import Die
from game.movetype import MoveType
from .board import Board
from .player import Player
from .point import Point

class Game:
    def __init__(self, win:pygame.Surface):
        self.win:pygame.Surface = win
        self._init()
    
    def select(self, point_num:int):
        print(self.selected)
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
    def get_legal_moves(self):
        for idx, die in enumerate(self.turn.dice):
            if die.enabled:
                self.validate_move(die.number)


    def validate_move(self,num:int) -> Tuple[MoveType,Destination]:
        new_num:int = self.selected.number + num
        points:List[Point] = self.board.points
        if new_num > len(points):
            if self.turn.ready_to_bear_off:
                return MoveType.BEAR_OFF 

        new_point = self.board.points[new_num]
        if new_point.checker_color == self.turn.checker_color:
            return MoveType.LEGAL_MOVE
        elif not new_point.is_blocked:
            return MoveType.HIT
        else:
            return MoveType.ILLEGAL_MOVE

    def next_turn(self):
        if self.turn == self.player_one:
            self.turn = self.player_two
        else:
            self.turn = self.player_one
      

    def update(self):
        pygame.display.update()
    
    def reset(self):
        self._init()
    
    def roll_dice(self):
        self.turn.roll_dice()
        self.board.draw_dice(self.player_one,self.player_two)

    
    def start_roll(self) -> Player:
        while self.player_one.dice[0].number == self.player_two.dice[0].number:
            self.player_one.roll_dice()
            self.player_two.roll_dice()

        die_one_value = self.player_one.dice[0].number
        die_two_value = self.player_two.dice[0].number
        self.board.draw_dice(self.player_one,self.player_two)
        player: Player = self.player_one if die_one_value > die_two_value else self.player_two
        player.dice[0].toggle()
        return player


    def _init(self):
        self.selected:Point = None
        self.player_one:Player = Player(COLOR_ONE,[Die(),Die()])
        self.player_two:Player = Player(COLOR_TWO,[Die(),Die()])
        self.board:Board = Board(self.win)
        
        self.turn:Player = self.start_roll()