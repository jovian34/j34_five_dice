import random


class Die():

    def __init__(self) -> None:
        self.size = 6

    def roll(self):
        return random.randint(1, self.size)