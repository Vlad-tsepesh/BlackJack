class GameUI:

    @staticmethod
    def get_player_move():
        return input("🃏 Hit or Stand? ").strip().lower()

    @staticmethod
    def show_line():
        print("_" * 100)

    @staticmethod
    def show_header(bank):
        print(f"   ♥  ♠  Black Jack ♦  ♣    Bank: ${bank}\n")

    @staticmethod
    def ask_bet_amount():
        return input("💰 Enter your bet amount: $".rjust(34))

    def show_status(self, player, dealer, end=True):
        self.show_header(player.bank)
        if end:
            print(f"{dealer.cards().center(22)} - {dealer.points()}")
        else:
            print(f"{dealer.hide_cards().center(22)}")
        print(f"{player.cards().center(22)} - {player.points()}")
        print(f"Bet: ${player.bet}".rjust(40))

    def show_result(self, result_code):
        messages = {
            'dealer_blackjack': "💣 Dealer has Blackjack!",
            'player_blackjack': "🎉 Player has Blackjack!",
            'dealer_busts': "🔥 Dealer busts. Player wins!",
            'player_busts': "❌ Player busts. Dealer wins.",
            'dealer_wins': "🟥 Dealer wins.",
            'player_wins': "✅ Player wins!",
            'push': "🤝 Push (Both have Blackjack)",
            'push_simple': "🤝 Push.",
            'invalid_input': "❌ Invalid input.",
            'invalid_bet': "❌ Invalid bet amount.",
            'out_of_money': "💀 Out of money. Game Over.",
            "continue": "Press Enter to continue...",
            "new game": "Press Enter to start a new game."
        }
        print(messages.get(result_code, result_code))
        self.show_line()

    @staticmethod
    def show_continue_prompt():
        input("😎 Ready for the next hand? Hit Enter to continue... ")

    @staticmethod
    def show_new_game_prompt():
        input("🎲 Press Enter to start a new game... ")

    @staticmethod
    def show_welcome_prompt():
        print("♠️♦️ Welcome to the Blackjack Table! ♣️♥️")

    def show_round_start(self, bank):
        self.show_line()
        self.show_header(bank)
