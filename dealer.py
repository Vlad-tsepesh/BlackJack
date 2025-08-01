from game_constants import DEALER_DRAW_THRESHOLD
from game_constants import TWO
from player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def should_draw(self):
        return self.points() < DEALER_DRAW_THRESHOLD

    def hide_cards(self):
        return f"{self.name}'s hand: {self.hand[0]}"

    def deal_initial_cards(self, deck, player):
        for _ in range(TWO):
            player.add_card(deck.draw())
            self.add_card(deck.draw())

    def play_turn(self, deck):
        while self.should_draw():
            self.add_card(deck.draw())
