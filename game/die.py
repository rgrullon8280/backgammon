import os
import random
from enum import Enum

import pygame

from game.constants import DICE_HEIGHT, DICE_WIDTH


class Die:
    def __init__(self) -> None:
        self.number:int = 1
        self.get_die_image()
    
    def roll(self) -> None:
        self.number = random.randint(1,6)
    
    def get_die_image(self) -> None:
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets',f'dice{self.number}.png')),(DICE_HEIGHT, DICE_WIDTH))
