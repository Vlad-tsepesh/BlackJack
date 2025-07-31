import random
from random import shuffle

from Card import Card
from constants import PATTERN

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        self.cards = []
        for _ in range(2):
            for suit_symbol in ['♧', '♢', '♡', '♤']:
                for rank, val in PATTERN.items():
                    self.cards.append(Card(rank, suit_symbol, val))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
