import pygame
from pygame import draw
from .constants import WIDTH, HEIGHT, NUM_OF_POINTS,COLOR_ONE, COLOR_TWO
from .point import Point
import os

WOOD_PICTURE = pygame.image.load(os.path.join('assets','wood.jpeg'))
SCALED_WOOD = pygame.transform.scale(WOOD_PICTURE,(WIDTH,HEIGHT))

class Board:
    def __init__(self, WIN: pygame.Surface):
       self.win = WIN
       self.points = []
       self.is_blocked = False
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
        

    def draw_points(self):
        for point in self.points:
            pygame.draw.polygon(self.win,COLOR_ONE if point.number % 2 == 0 else COLOR_TWO,[(point.x1,point.y1), (point.x2,point.y2), (point.x3,point.y3)])
            point.draw_checkers(self.win)