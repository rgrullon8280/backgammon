import random

class Die:
    def __init__(self, number: int) -> None:
        self.number = number
    
    def roll(self) -> None:
        self.number = random.randint(1,6)
        