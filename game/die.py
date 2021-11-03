import random

class Die:
    def __init__(self, number):
        self.number = number
    
    def roll(self):
        self.number = random.randint(1,6)