from typing import List, Tuple
import pygame
from game.Destination import Destination
from game.bar import Bar

from game.constants import COLOR_ONE, COLOR_TWO, DICE_1_X, DICE_2_X, DICE_3_X, DICE_4_X, DICE_HEIGHT, DICE_Y
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
        if not self.turn.dice[0].enabled and not self.turn.dice[1].enabled:
            self.next_turn()
        self.turn.has_checkers_on_bar = self.board.bar.has_checkers_on_bar(self.turn)
        if point_num is None:
            return
        dest:Destination = self.board.points[point_num]
        if self.selected:
            if dest in self.legal_moves:
                move_type, idx = self.legal_moves[dest]
                self.board.execute_move(move_type, dest,self.selected)
                if idx == 2:
                    self.turn.dice[0].toggle()
                    self.turn.dice[1].toggle()
                else:
                    self.turn.dice[idx].toggle()
                
                
        else:
            if self.turn.has_checkers_on_bar:
                self.selected = self.board.bar
            
            elif dest.checker_color == self.turn.checker_color:
                self.selected = dest
            self.get_legal_moves()
          

    def get_legal_moves(self):
        for idx, die in enumerate(self.turn.dice):
            if die.enabled:
                move_type, dest = self.validate_move(die.number)
                self.legal_moves[dest] = (move_type,idx)
        if self.turn.dice[0].enabled and self.turn.dice[1].enabled:
            self.legal_moves[2] = self.validate_move(self.turn.dice[0].number + self.turn.dice[1].number)


    def validate_move(self,num:int) -> Tuple[MoveType,Destination]:
        if self.turn.has_checkers_on_bar:
            new_num:int = (num * self.turn.direction*-1) - 1
            new_point = self.board.points[new_num]
            if new_point.checker_color == self.turn.checker_color:
                return (MoveType.LEGAL_MOVE,new_point)
            elif not new_point.is_blocked:
                return (MoveType.HIT,new_point)
            else:
                return (MoveType.ILLEGAL_MOVE, new_point)

        new_num:int = (self.selected.number + self.turn.direction) + (num * self.turn.direction)
        points:List[Point] = self.board.points
        if new_num > len(points) or new_num < 0:
            if self.turn.ready_to_bear_off:
                return (MoveType.BEAR_OFF, self.board.Bar)

        new_point = self.board.points[new_num]
        if new_point.checker_color == self.turn.checker_color or new_point.checker_color is None:
            return (MoveType.LEGAL_MOVE,new_point)
        elif not new_point.is_blocked:
            return (MoveType.HIT,new_point)
        else:
            return (MoveType.ILLEGAL_MOVE, new_point)

    def next_turn(self):
        if self.turn == self.player_one:
            self.turn = self.player_two
        else:
            self.turn = self.player_one
        self.turn.dice[0].toggle()
        self.turn.dice[1].toggle()
        self.selected = None
        self.legal_moves = {}
      
    def draw_dice(self):
        for die in self.player_one.dice:
            die.draw(self.win)
        for die in self.player_two.dice:
            die.draw(self.win)


    def update(self):
        self.board.draw_board()
        self.draw_dice()
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
        player: Player = self.player_one if die_one_value > die_two_value else self.player_two
        player.dice[0].toggle()
        return player


    def _init(self):
        self.selected:Destination = None
        self.player_one:Player = Player(COLOR_TWO,[Die((DICE_3_X,DICE_Y)),Die((DICE_4_X,DICE_Y))],-1)
        self.player_two:Player = Player(COLOR_ONE,[Die((DICE_1_X,DICE_Y)),Die((DICE_2_X,DICE_Y))],1)
        self.legal_moves:dict[Destination, Tuple[MoveType, int]] = {}
        self.board:Board = Board(self.win)
        
        self.turn:Player = self.start_roll()