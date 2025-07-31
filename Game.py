from Deck import Deck
from Player import Player
from Dealer import Dealer
from art import logo


def clear():
    print("\n" * 2)




class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Dealer()

    def prepare_round(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.shuffle()

    def take_bets(self):
        self.player.bet = input(f"Bet: $".rjust(37))

    def set_points(self):
        self.dealer.points()
        self.player.points()


    def deal_initial_cards(self):
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

    def start_round(self):

        self.print_top()
        self.print_deck()
        self.prepare_round()
        self.print_cards()
        self.take_bets()
        self.deal_initial_cards()
        self.print_line()
        # Reset hands, bets, deal cards

    def player_turn(self):
        self.print_deck()
        self.print_cards()
        self.print_bet()
        self.print_line()
        input()
        self.player.add_card(self.deck.draw())
        # Handle player input and actions
        pass

    def dealer_turn(self):
        if self.dealer.should_draw():
            self.dealer.add_card(self.deck.draw())

    def evaluate_winner(self):
        # Compare points and adjust bank
        pass

    def play(self):
        game.start_round()
        while True:
            game.player_turn()
            game.dealer_turn()


    def print_top(self):
        print(f"   ♥  ♠  Black Jack ♦  ♣    Bank: ${self.player.bank}\n")

    def print_deck(self):
        print(f"🂡 {len(self.deck.cards)} ".rjust(39))

    def print_cards(self):
        print(self.dealer.cards().center(22), " - ", self.dealer.points())
        print(self.player.cards().center(22), " - ", self.player.points())

    def print_bet(self):
        print(f"Bet: ${self.player.bet}".rjust(40))

    def print_line(self):
        print("_" * 100)


game = Game()
game.play()