BOLD = "\033[1m"
RESET = "\033[0m"

PATTERN = {
    f"{BOLD}A{RESET}": 1,
    f"{BOLD}K{RESET}": 10,
    f"{BOLD}Q{RESET}": 10,
    f"{BOLD}J{RESET}": 10,
    f"{BOLD}10{RESET}": 10,
    f"{BOLD}9{RESET}": 9,
    f"{BOLD}8{RESET}": 8,
    f"{BOLD}7{RESET}": 7,
    f"{BOLD}6{RESET}": 6,
    f"{BOLD}5{RESET}": 5,
    f"{BOLD}4{RESET}": 4,
    f"{BOLD}3{RESET}": 3,
    f"{BOLD}2{RESET}": 2,
}


CARD_TYPES = {
    'clubs': '♣️',    # U+2663
    'diamonds': '♦️', # U+2666
    'hearts': '♥️',   # U+2665
    'spades': '♠️',   # U+2660
}


DEALER_DRAW_THRESHOLD = 17
TEN = 10
BLACKJACK_MAX_POINTS = 21
TWO = 2
STAND = "stand"
HIT = "hit"
NO_BET = 0

DEALER_BLACKJACK = "dealer_blackjack"
PLAYER_BLACKJACK = "player_blackjack"
DEALER_BUSTS = "dealer_busts"
PLAYER_BUSTS = "player_busts"
DEALER_WINS = "dealer_wins"
PLAYER_WINS = "player_wins"
PUSH = "push"
PUSH_SIMPLE = "push_simple"
INVALID_INPUT = "invalid_input"
INVALID_BET = "invalid_bet"
OUT_OF_MONEY = "out_of_money"
