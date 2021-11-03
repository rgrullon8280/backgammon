from .constants import HEIGHT, WIDTH

class Checker:
    def __init__(self, diameter, prim_color,sec_color, x):
        self.outer_radius = diameter / 2
        self.inner_radius = self.outer_radius - 5
        self.prim_color = prim_color
        self.sec_color = sec_color
        self.x = x
        self.y = 0
    
    def calc_y(self,num_of_checker,num_of_point,point_y):
        y = 0
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
        
        self.y = y
        return self
