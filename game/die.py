import os
import random
from enum import Enum
from typing import Tuple

import pygame

from game.constants import DICE_HEIGHT, DICE_WIDTH


class Die:
    def __init__(self,coor:Tuple[float,float]) -> None:
        self.number:int = 1
        self.x, self.y = coor
        self.get_die_image()
        self.enabled:bool = False

    def toggle(self):
        self.enabled = not self.enabled

    def draw(self, win: pygame.Surface):
        win.blit(self.image,(self.x,self.y))

    
    def roll(self) -> None:
        self.number = random.randint(1,6)
        self.get_die_image()
    
    def get_die_image(self) -> None:
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets',f'dice{self.number}.png')),(DICE_HEIGHT, DICE_WIDTH))
