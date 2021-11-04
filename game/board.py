
import pygame

from game.player import Player
from .constants import DICE_1_X, DICE_2_X, DICE_3_X, DICE_4_X, DICE_Y, WIDTH, HEIGHT, NUM_OF_POINTS,COLOR_ONE, COLOR_TWO
from .point import Point
from .movetype import MoveType
from typing import Dict, List
import os
from .checker import Checker





WOOD_PICTURE = pygame.image.load(os.path.join('assets','wood.jpeg'))
SCALED_WOOD = pygame.transform.scale(WOOD_PICTURE,(WIDTH,HEIGHT))


class Board:
    def __init__(self, WIN: pygame.Surface):
       self.win:pygame.Surface = WIN
       self.points:List[Point] = []
       self.is_blocked: bool = False
       self._init_points()
       self.draw_board()
    
    def _init_points(self):
        for num in range(NUM_OF_POINTS):
            num_of_checkers = 0
            prim_color = ""
            sec_color = ""
            if num == 0:
                num_of_checkers = 2
                prim_color = COLOR_ONE
                sec_color = COLOR_TWO
            elif num == 5:
                num_of_checkers = 5
                prim_color = COLOR_TWO
                sec_color = COLOR_ONE
            elif num == 7:
                num_of_checkers = 3
                prim_color = COLOR_TWO
                sec_color = COLOR_ONE
            elif num == 11:
                num_of_checkers = 5
                prim_color = COLOR_ONE
                sec_color = COLOR_TWO
            elif num == 23:
                num_of_checkers = 2
                prim_color = COLOR_TWO
                sec_color = COLOR_ONE
            elif num == 18:
                num_of_checkers = 5
                prim_color = COLOR_ONE
                sec_color = COLOR_TWO
            elif num == 16:
                num_of_checkers = 3
                prim_color = COLOR_ONE
                sec_color = COLOR_TWO
            elif num == 12:
                num_of_checkers = 5
                prim_color = COLOR_TWO
                sec_color = COLOR_ONE
            self.points.append(Point(num, num_of_checkers, prim_color,sec_color))
    
    def draw_board(self):
        self.win.blit(SCALED_WOOD, (0,0))
        self.draw_points()
             
    
    def draw_dice(self, player_one:Player, player_two:Player):
        self.win.blit(player_one.dice[0].image,(DICE_1_X,DICE_Y))
        self.win.blit(player_one.dice[1].image,(DICE_2_X,DICE_Y))
        self.win.blit(player_two.dice[0].image,(DICE_3_X,DICE_Y))
        self.win.blit(player_two.dice[1].image,(DICE_4_X,DICE_Y))

    def draw_points(self):
        for point in self.points:
            pygame.draw.polygon(self.win,COLOR_ONE if point.number % 2 == 0 else COLOR_TWO,[(point.x1,point.y1), (point.x2,point.y2), (point.x3,point.y3)])
            point.draw_checkers(self.win)

    def calc_legal_moves(self,player: Player,current_point: Point):
        self.legal_moves: dict[int,Point] = {}


        move_amount_one:int = player.dice[0].number
        move_amount_two:int = player.dice[1].number
        move_amount_three:int = player.dice[0].number + player.dice[1].number

        curr_num = current_point.number-1

        if curr_num + min(move_amount_one, move_amount_two,move_amount_three) > len(self.points) and player.ready_to_bear_off():
            self.legal_moves.append()

        new_point_one: Point = self.points[curr_num + move_amount_one]
        new_point_two: Point = self.points[curr_num + move_amount_two]
        new_point_three: Point = self.points[curr_num + move_amount_three]

        if not new_point_one.is_blocked and ((new_point_one.checker_color == player.checker_color) or (new_point_one.checker_color is None) or (len(new_point_one.checkers) == 1)):
            self.legal_moves.append(new_point_one) 
        if not new_point_two.is_blocked and ((new_point_two.checker_color == player.checker_color) or (new_point_two.checker_color is None) or (len(new_point_two.checkers) == 1)):
            self.legal_moves.append(new_point_two) 
        if not new_point_three.is_blocked and ((new_point_three.checker_color == player.checker_color) or (new_point_three.checker_color is None) or (len(new_point_three.checkers) == 1)):
            self.legal_moves.append(new_point_three) 
    
    def validate_move(self,player:Player, num:int,curr_num:int) -> MoveType:
        new_num:int = curr_num + num
        if new_num > len(self.points):
            if player.ready_to_bear_off:
                return MoveType.BEAR_OFF 

        new_point = self.points[new_num]
        if new_point.checker_color == player.checker_color:
            return MoveType.LEGAL_MOVE
        elif not new_point.is_blocked:
            return MoveType.HIT
        else:
            return MoveType.ILLEGAL_MOVE

        


    

    def move_checker(self, current_point:Point,dest_point:Point):
        if dest_point in self.legal_moves:
            checker: Checker = current_point.remove_checker()
            checker.move_to(dest_point)
            dest_point.add_checker(checker)
        self.draw_board()



