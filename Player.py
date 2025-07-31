from constants import TEN

class Player:
    def __init__(self, name, bank=1000):
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

    def place_bet(self, amount):
        # Deduct from bank, etc.
        pass

    def reset_hand(self):
        self.hand = []
        self.ace = False