from Dealer import Dealer
from Deck import Deck
from Player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Dealer()

    def play(self):
        self.prepare_round()

        if not self.take_bets():
            return

        self.deal_initial_cards()

        if self.check_immediate_blackjack():
            self.reset_hands()
            return

        self.player_phase()
        self.dealer_phase()
        self.evaluate_winner()
        self.reset_hands()

    def prepare_round(self):
        self.reset_hands()
        self.deck.shuffle()
        self.print_line()
        self.print_header()

    def take_bets(self):
        bet = input("-> Bet: $".rjust(37))
        if bet.isdigit() and 0 < int(bet) <= self.player.bank:
            self.player.bet = int(bet)
            self.player.bank -= self.player.bet
            self.print_line()
            return True
        print("❌ Invalid bet amount.")
        return self.take_bets()

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

    def check_immediate_blackjack(self):
        player_blackjack = self.player.points() == 21
        dealer_blackjack = self.dealer.points() == 21

        if dealer_blackjack:
            print("💣 Dealer has Blackjack!")
            if player_blackjack:
                self.player.bank += self.player.bet
                self.player.bet = 0
                self.print_status()
                print("🤝 Push (Both have Blackjack)")
            else:
                self.print_status()
                print("❌ Dealer wins.")
            self.print_line()
            return True

        if player_blackjack:
            self.player.bank += int(self.player.bet * 2.5)
            self.player.bet = 0
            self.print_status()
            print("🎉 Player has Blackjack!")
            self.print_line()
            return True

        return False

    def player_phase(self):
        while self.player.points() < 21:
            self.print_status(True)
            move = input("Hit or Stand? ").strip().lower()
            self.print_line()
            if move == "stand":
                break
            elif move == "hit":
                self.player.add_card(self.deck.draw())
            else:
                print("❌ Invalid input.")

    def dealer_phase(self):
        while self.dealer.should_draw():
            self.dealer.add_card(self.deck.draw())

    def evaluate_winner(self):
        player = self.player.points()
        dealer = self.dealer.points()

        if player > 21:
            self.print_status()
            print("❌ Player busts. Dealer wins.")
        elif dealer > 21:
            self.player.bank += self.player.bet * 2
            self.player.bet = 0
            self.print_status()
            print("🔥 Dealer busts. Player wins!")
        elif player > dealer:
            self.player.bank += self.player.bet * 2
            self.player.bet = 0
            self.print_status()
            print("✅ Player wins!")
        elif player < dealer:
            self.print_status()
            print("🟥 Dealer wins.")
        else:
            self.player.bank += self.player.bet
            self.player.bet = 0
            self.print_status()
            print("🤝 Push.")

    def reset_hands(self):
        self.player.reset_hand()
        self.dealer.reset_hand()

    def print_header(self):
        print(f"   ♥  ♠  Black Jack ♦  ♣    Bank: ${self.player.bank}\n")

    def print_status(self, isDone = False):
        self.print_header()
        if isDone:
            print(f"{self.dealer.hidden_cards().center(22)}")
        else:
            print(f"{self.dealer.cards().center(22)} - {self.dealer.points()}")
        print(f"{self.player.cards().center(22)} - {self.player.points()}")
        print(f"Bet: ${self.player.bet}".rjust(40))

    def print_line(self):
        print("_" * 100)


# Game loop
while True:
    input("Press Enter to start a new game.")
    game = Game()
    while True:
        game.play()
        input("Press Enter to continue...")
        if game.player.bank <= 0:
            print(f"💀 Out of money (${game.player.bank}). Game Over.")
            break
