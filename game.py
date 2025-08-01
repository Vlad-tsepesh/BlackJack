from dealer import Dealer
from deck import Deck
from evaluator import Evaluator
from game_constants import *
from game_ui import GameUI
from player import Player


class Game:
    def __init__(self):
        self.ui = GameUI()
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
        self.evaluator = Evaluator(self.player, self.dealer, self.ui)

    def play(self):
        self.player.reset_hand()

        self.dealer.reset_hand()

        self.deck.shuffle()

        self.ui.show_round_start(self.player.bank)

        self.set_bet()

        self.dealer.deal_initial_cards(self.deck, self.player)

        if self.evaluator.check_immediate_blackjack(): return

        self.player_phase()

        self.dealer.play_turn(self.deck)

        self.evaluator.evaluate_winner()

    def prepare_round(self):
        player_bank = self.player.bank
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.shuffle()
        self.ui.show_round_start(player_bank)

    def set_bet(self):
        while True:
            amount = self.ui.ask_bet_amount()
            if self.player.is_valid_bet(amount):
                self.player.place_bet(int(amount))
                self.ui.show_line()
                break
            self.ui.show_result(INVALID_BET)

    def player_phase(self):
        while self.player.points() < BLACKJACK_MAX_POINTS:
            self.ui.show_status(self.player, self.dealer, False)
            move = self.ui.get_player_move()
            self.ui.show_line()

            if move == STAND:
                break
            elif move == HIT:
                self.player.add_card(self.deck.draw())
            else:
                self.ui.show_result(INVALID_INPUT)
