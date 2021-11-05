from typing import Tuple
from .constants import HEIGHT, WIDTH

class Checker:
    def __init__(self, diameter: float, prim_color: Tuple[int,int,int],sec_color: Tuple[int,int,int], x: float, num_of_point:int) -> None:
        self.outer_radius:float = diameter / 2
        self.inner_radius:float = self.outer_radius - 5
        self.prim_color:Tuple[int,int,int] = prim_color
        self.sec_color:Tuple[int,int,int] = sec_color
        self.x:float = x
        self.y:float = 0.0
        self.num_of_point: int = num_of_point
    
    def move_to(self,point):
        self.num_of_point = point.number
        self.x = point.x3
        self.y = self.calc_y(len(point.checkers),point.y1)
        



    def calc_y(self,num_of_checker: int,point_y:float) -> None:
        y:int = 0
        num_of_point = self.num_of_point
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
