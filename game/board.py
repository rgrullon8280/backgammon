import pygame

from game.player import Player
from .constants import WIDTH, HEIGHT, NUM_OF_POINTS,COLOR_ONE, COLOR_TWO
from .point import Point
from typing import List
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
        self.win.blit(player_one.dice[0].image,(800,600))
        self.win.blit(player_one.dice[1].image,(800+50,600))
        self.win.blit(player_two.dice[0].image,(800,600))
        self.win.blit(player_two.dice[1].image,(800+50,600))

    def draw_points(self):
        for point in self.points:
            pygame.draw.polygon(self.win,COLOR_ONE if point.number % 2 == 0 else COLOR_TWO,[(point.x1,point.y1), (point.x2,point.y2), (point.x3,point.y3)])
            point.draw_checkers(self.win)

    def calc_legal_moves(self,player: Player,current_point: Point):
        self.legal_moves: List[Point] = []
        move_amount_one:int = player.dice[0].number
        move_amount_two:int = player.dice[1].number
        move_amount_three:int = player.dice[0].number + player.dice[1].number

        curr_num = current_point.number

        new_point_one: Point = self.points[curr_num + move_amount_one]
        new_point_two: Point = self.points[curr_num + move_amount_two]
        new_point_three: Point = self.points[curr_num + move_amount_three]

        if not new_point_one.isblocked and ((new_point_one.checker_color == player.checker_color) or (new_point_one.checker_color is None) or (len(new_point_one.checkers) == 1)):
            self.legal_moves.append(new_point_one) 
        if not new_point_two.isblocked and ((new_point_two.checker_color == player.checker_color) or (new_point_two.checker_color is None) or (len(new_point_two.checkers) == 1)):
            self.legal_moves.append(new_point_two) 
        if not new_point_three.isblocked and ((new_point_three.checker_color == player.checker_color) or (new_point_three.checker_color is None) or (len(new_point_three.checkers) == 1)):
            self.legal_moves.append(new_point_three) 
    
    def move_checker(self, current_point:Point,dest_point:Point):
        if dest_point in self.legal_moves:
            checker: Checker = current_point.remove_checker()
            checker.move_to(dest_point)
            dest_point.add_checker(checker)
        self.draw_board()








