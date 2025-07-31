from constants import DEALER_DRAW_THRESHOLD
from Player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def should_draw(self):
        return self.points() < DEALER_DRAW_THRESHOLD

    def hidden_cards(self):
        return f"{self.name}'s hand: {self.hand[0]}"
