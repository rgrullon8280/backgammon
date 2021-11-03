from typing import Tuple
from .constants import HEIGHT, WIDTH

class Checker:
    def __init__(self, diameter: float, prim_color: Tuple[int,int,int],sec_color: Tuple[int,int,int], x: float) -> None:
        self.outer_radius:float = diameter / 2
        self.inner_radius:float = self.outer_radius - 5
        self.prim_color:Tuple[int,int,int] = prim_color
        self.sec_color:Tuple[int,int,int] = sec_color
        self.x:float = x
        self.y:float = 0.0
    
    def move_to(self,point):
        FPS = 15
        x_step:float = (self.x - point.x3)/FPS
        new_y:float = self.calc_y(len(point.checkers),point.number,point.y1)
        y_step:float = (self.y - new_y)/FPS
        while self.x < point.x3 and self.y < new_y:
            self.x += x_step
            self.y += y_step
        



    def calc_y(self,num_of_checker: int,num_of_point: int,point_y:float) -> None:
        y:int = 0
        if num_of_point < 13:
            if num_of_checker == 14:
                y = point_y - (3 * self.outer_radius * 2) + self.outer_radius
            elif num_of_checker > 11:
                y = point_y - ((num_of_checker % 10)* self.outer_radius * 2)
            elif num_of_checker > 8:
                y = point_y - ((num_of_checker % 7)* self.outer_radius * 2) + self.outer_radius
            elif num_of_checker == 8:
                y = point_y - (4 * self.outer_radius * 2)
            elif num_of_checker > 4:
                y = point_y - ((num_of_checker % 4)* self.outer_radius * 2)
            else:
                y = point_y - ((num_of_checker + 1)* self.outer_radius * 2) + self.outer_radius

        else:
            if num_of_checker == 14:
                y = point_y + (3 * self.outer_radius * 2) - self.outer_radius
            elif num_of_checker > 11:
                y = point_y + ((num_of_checker % 10)* self.outer_radius * 2)
            elif num_of_checker > 8:
                y = point_y + ((num_of_checker % 7)* self.outer_radius * 2) - self.outer_radius
            elif num_of_checker == 8:
                y = point_y + (4 * self.outer_radius * 2)
            elif num_of_checker > 4:
                y = point_y + ((num_of_checker % 4)* self.outer_radius * 2)
            else:
                y = point_y + ((num_of_checker + 1) * self.outer_radius * 2) - self.outer_radius
        
        return y
