
import pygame

from game.player import Player
from .constants import BAR_WIDTH, LEFT_BOARD_MAX_X, WIDTH, HEIGHT, NUM_OF_POINTS,COLOR_ONE, COLOR_TWO, BLACK
from .point import Point
from .movetype import MoveType
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
        self.draw_bar()
             
    
    def draw_bar(self):
        pygame.draw.rect(self.win, BLACK, (LEFT_BOARD_MAX_X,0,BAR_WIDTH,HEIGHT),1)

    def draw_points(self):
        for point in self.points:
            pygame.draw.polygon(self.win,COLOR_ONE if point.number % 2 == 0 else COLOR_TWO,[(point.x1,point.y1), (point.x2,point.y2), (point.x3,point.y3)])
            point.draw_checkers(self.win)

    

    def move_checker(self, current_point:Point,dest_point:Point):
        if dest_point in self.legal_moves:
            checker: Checker = current_point.remove_checker()
            checker.move_to(dest_point)
            dest_point.add_checker(checker)
        self.draw_board()



