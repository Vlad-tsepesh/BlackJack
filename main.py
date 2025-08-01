from game import Game
from game_constants import NO_BET, OUT_OF_MONEY
from game_ui import GameUI


def run_game_loop():
    GameUI.show_welcome_prompt()
    while True:
        GameUI.show_new_game_prompt()
        game = Game()
        while True:
            game.play()
            if game.player.bank <= NO_BET:
                game.ui.show_result(OUT_OF_MONEY)
                break
            GameUI.show_continue_prompt()


if __name__ == "__main__":
    run_game_loop()
