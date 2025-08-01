from dealer import Dealer
from game_constants import *
from game_ui import GameUI
from player import Player


class Evaluator:
    def __init__(self, player: Player, dealer: Dealer, ui: GameUI):
        self.player = player
        self.dealer = dealer
        self.ui = ui

    def show_blackjack_results(self, *messages):
        self.ui.show_status(self.player, self.dealer)
        for message in messages:
            self.ui.show_result(message)
        self.ui.show_line()

    def check_immediate_blackjack(self):
        player_blackjack = self.player.points() == BLACKJACK_MAX_POINTS
        dealer_blackjack = self.dealer.points() == BLACKJACK_MAX_POINTS

        if dealer_blackjack:
            self.player.bet = NO_BET
            if player_blackjack:
                self.player.payout_push()
                self.show_blackjack_results(DEALER_BLACKJACK, PUSH)
            else:
                self.show_blackjack_results(DEALER_BLACKJACK, DEALER_WINS)
            return True

        if player_blackjack:
            self.player.payout_blackjack()
            self.show_blackjack_results(PLAYER_BLACKJACK)
            return True

        return False

    def evaluate_winner(self):
        player = self.player.points()
        dealer = self.dealer.points()
        self.ui.show_status(self.player, self.dealer)

        if player > BLACKJACK_MAX_POINTS:
            self.ui.show_result(PLAYER_BUSTS)
        elif dealer > BLACKJACK_MAX_POINTS:
            self.player.payout_win()
            self.ui.show_result(DEALER_BUSTS)
        elif player > dealer:
            self.player.payout_win()
            self.ui.show_result(PLAYER_WINS)
        elif player < dealer:
            self.ui.show_result(DEALER_WINS)
        else:
            self.player.payout_push()
            self.ui.show_result(PUSH_SIMPLE)
