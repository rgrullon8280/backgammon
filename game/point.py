import pygame

from game.Destination import Destination
from .constants import WIDTH, HEIGHT, NUM_OF_POINTS, BAR_WIDTH, MID_HEIGHT
from .checker import Checker
from typing import List, Tuple

class Point(Destination):
    def __init__(self, num: int, num_of_checkers:int, prim_color:Tuple[int,int,int],sec_color:Tuple[int,int,int]) -> None:
        super(Point, self).__init__()
        self.number = num + 1
        
        

        self.x1 = self.y1 = self.x2 = self.y2 = self.x3 = self.y3 = 0
        self.width:float = (WIDTH - BAR_WIDTH)/(NUM_OF_POINTS/2)
        self.height:float = (HEIGHT - MID_HEIGHT)/2
        
        self._get_coordinates()
        self._init_checkers(num_of_checkers, prim_color,sec_color)
        self.check_blocked()
        self.check_checker_color()
    
    def check_checker_color(self):
        if len(self.checkers) == 0:
            self.checker_color = None
        else:
            self.checker_color = self.checkers[0].prim_color

    def check_blocked(self) -> None:
        self.is_blocked:bool = len(self.checkers) > 1

    def add_checker(self, checker: Checker):
        self.checkers.append(checker)
        self.check_blocked()

    def remove_checker(self) -> Checker:
        return self.checkers.pop()
    
    def _init_checkers(self, num:int, prim_color:Tuple[int,int,int], sec_color:Tuple[int,int,int]):
        self.checkers:List[Checker] = []
        for _ in range(num):
            self.checkers.append(Checker(self.width,prim_color,sec_color,self.x3, self.number))
    
    def draw_checkers(self, win: pygame.Surface):
        for idx, checker in enumerate(self.checkers):
            checker.y = checker.calc_y(idx, self.y1)
            pygame.draw.circle(win, checker.sec_color, (checker.x, checker.y),checker.outer_radius)
            pygame.draw.circle(win, checker.prim_color, (checker.x, checker.y),checker.inner_radius)
    
    def _get_coordinates(self):
        if self.number <= 12:
            self.y1 = self.y2 = HEIGHT
            self.y3 = self.height + MID_HEIGHT
            if self.number <= 6:
                self.x1 = self.width * (NUM_OF_POINTS/2 - self.number) + BAR_WIDTH
            else:
                self.x1 = self.width * (NUM_OF_POINTS/2 - self.number)
            self.x2 = self.x1 + self.width
            self.x3 = self.x1 + self.width/2   
        else:
            self.y3 = self.height
            if self.number >= 19:
                self.x1 = self.width * (self.number - (NUM_OF_POINTS/2 + 1)) + BAR_WIDTH
            else:
                self.x1 = self.width * (self.number - (NUM_OF_POINTS/2 + 1))
            self.x2 = self.x1 + self.width
            self.x3 = self.x1 + self.width/2  
