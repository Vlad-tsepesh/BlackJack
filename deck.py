import random

from card import Card
from game_constants import PATTERN, CARD_TYPES


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        self.cards = []
        for _ in range(6):
            for suit_symbol in CARD_TYPES.values():
                for rank, val in PATTERN.items():
                    self.cards.append(Card(rank, suit_symbol, val))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
