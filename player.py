from game_constants import *


class Player:
    def __init__(self, name="Player", bank=1000):
        self.name = name
        self.hand = []
        self.bank = bank
        self.bet = 100
        self.ace = False

    def cards(self):
        return f"{self.name}'s hand: " + '|'.join(str(card) for card in self.hand)

    def add_card(self, card):
        self.set_ace(card)
        self.hand.append(card)

    def set_ace(self, card):
        if card.rank == 'A':
            self.ace = True

    def clear_hand(self):
        self.hand = []

    def points(self):
        points = 0
        for card in self.hand:
            points += card.value
        if self.ace and points <= 11:
            points += TEN
        return points

    def is_valid_bet(self, amount: str) -> bool:
        return amount.isdigit() and 0 < int(amount) <= self.bank

    def place_bet(self, amount: int):
        self.bet = amount
        self.bank -= amount

    def reset_hand(self):
        self.hand = []
        self.ace = False

    def payout_blackjack(self):
        self.bank += int(self.bet * 2.5)
        self.bet = 0

    def payout_win(self):
        self.bank += self.bet * 2
        self.bet = 0

    def payout_push(self):
        self.bank += self.bet
        self.bet = 0
