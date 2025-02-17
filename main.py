import random
from replit import clear
from art import logo
import time

#I use pattern to calculate values for each card
pattern = { 
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 4,
}
# I'm using these symbols in combination  with 'pattern' to create real time deck
cardtypes = {            
    'clubs': '♧',
    'diamonds': '♢',
    'hearts': '♡',
    'spades': '♤',
    }
# deck is the real time deck
deck = []

# in reallity it's not shuffling just restarting the Deck by creating a new one
def shuffling():
    deck = []
    for n in range(2):
        for types, sign in cardtypes.items():
            for key, value in pattern.items():
                deck.append(key + sign)
    return deck
    
# to add an new card into players, dealer hands.
def get_one_card(hands):   
    hands.append(deck.pop(deck.index(random.choice(deck))))
    clear()
    image()
    game_scores()
    time.sleep(0.5)
    return hands

# deal is the function which simulate the real time game intro when the dealer gave 2 cards to each one player and dealer
def deal():
    for n in range(2):
        get_one_card(player)
        get_one_card(dealer)

# hit bet stand is a function which gave player three choices to double bet, to stand, or to hit
def hit_bet_stand(player):
    player_decision = ''
    clear()
    image()
    game_scores()
    player_decision = input("|  X2 BET  type 'd' |\n| HIT press 'enter' | STAND type 's' | ").lower()
    if player_decision == 'd':
        return player_decision
    elif player_decision != 's':
        get_one_card(player)
    return player_decision

# similar to hit bet stand, but gave just hit and stand options though. 
def hit_or_stand(player):
    player_decision = ''
    while not 's' in player_decision and points_amount(player) < MAX_POINTS:
        clear()
        image()
        game_scores()
        player_decision = input("\n| HIT press 'enter' | STAND type 's' | ").lower() 
        if player_decision != 's':
            get_one_card(player)
            
    return player_decision

# calculating the points amount for player or for dealear
def points_amount(hands):
    points = 0
    aces = []
    for index, card in enumerate(hands):
        if 'A' in card:
            aces.append(card)
        else:
            if len(card) < 3:
                points += pattern[card[0]]
            else:
                points += pattern[card[:2]]
                
    while aces:
        aces.pop()
        if points + ACE_11P <= MAX_POINTS and not aces:
            points += ACE_11P
        else:
            points += ACE_1P
            
    return points



#this is printing player information score, cards, win, or lost.
def player_score():
    if dealer_cards == 'hidden':
        print(f"    Player's cards:    {points_amount(player)}\n" + f"  |{'|'.join(player)}|".center(22) + "")
    else:
        print(f"    Player's cards:    {points_amount(player)}{player_state}\n" + f"  |{'|'.join(player)}|".center(22) + "")
    print(f"Bet: ${bet}".rjust(40))


#it's a bit more complex but is doing the same as for player score.
def dealer_score():
    if dealer_cards == 'hidden':
        if len(dealer) == 0:
            print(f"    Dealer's cards:    \n"  + "\n")
        elif len(dealer) == 1:
            print(f"    Dealer's cards:    {pattern[dealer[0][0]] if len(dealer[0]) < 3 else pattern['10']}\n" + f"  |{dealer[0]}|".center(22) + "\n")     
        else:
            print(f"    Dealer's cards:    {pattern[dealer[0][0]] if len(dealer[0]) < 3 else pattern['10']}\n" + f"  |{dealer[0]}|?{dealer[1][(1 if len(dealer[1]) < 3 else 2)]}|".center(22) + "\n")
    else:
        print(f"    Dealer's cards:    {points_amount(dealer)}{dealer_state}\n" + f"  |{'|'.join(dealer)}|".center(22) + "\n")

#combintation of dealer and player score
def game_scores():
    dealer_score()
    player_score()
# information of the game such as logo, title and card left in the deck
def image():
    print(logo)
    print(f"   ♥  ♠  Black Jack ♦  ♣    Bank: ${bank}\n")
    print(f"🂡 {len(deck)} ".rjust(39))




DEALER_DRAW_THRESHOLD = 17 # cap points when dealr still draw the cards. 
BLACKJACK_THRESHOLD = 21  # black jack condition
MAX_POINTS = 21 # max possible points , to not bust
ACE_1P = 1 #  Ace value if you reach max_points 
ACE_11P = 11 # Base value


print(logo) 
print("\033[91m   ♥  ♠  Black Jack ♦  ♣\033[0m\n")
game = input("To start the game press enter, to quit type 'q'.") # variable used for as condition for the game
base_bet = 100  #used as base for bet
while not 'q' in game:
    bet = 0
    bank = 1000
    deck = shuffling()
    dealer = []
    while bank > 0:
        while True:
            clear()
            image()
            print(f"\n\n\n\n" + f"Bet: ${bet}".rjust(40))
            choice = input(f"\nTo bet ${base_bet} press enter.\nALL INN type 'a'.\nTo change the bet type new amount: $")
            if choice.isdecimal():
                if int(choice) <= bank:
                    base_bet = int(choice)
                    bet = base_bet
                    break
            elif 'a' in choice:
                bet = bank
                break
            elif base_bet <= bank:
                bet = base_bet
                break
        
        
        bank -= bet
        player = []
        dealer = []
        player_state = ''
        dealer_state = ''
        dealer_cards = 'hidden'
        
        if len(deck) < 60:  # if condition is true deck is refreshed to a new noe
            clear()
            print(logo)
            print(f"   ♥  ♠  Black Jack ♦  ♣    Bank: ${bank}.\n")
            print(f"🂡 {len(deck)} ".rjust(39) + " Shuffling")
            deck = shuffling()
            time.sleep(1)
            clear()
            print(logo)
            print(f"   ♥  ♠  Black Jack ♦  ♣    Bank: ${bank}.\n")
            print(f"🂡 {len(deck)} ".rjust(39) + " Shuffling")
            time.sleep(1)
            
        deal() # deal is the function which simulate the real time game intro when the dealer gave 2 cards to each one player and dealer
            
        if points_amount(player) == BLACKJACK_THRESHOLD:       # if player have black jack
                  
            if points_amount(dealer) == BLACKJACK_THRESHOLD:   # if dealer have black jack
                player_state = '    Push!    Black Jack'
                dealer_state = '    Push!    Black Jack'
                time.sleep(0.5) 
                bank += int(bet)
                
            
            else:  #if player have a black jack and dealer not.
                player_state = '    You win!    Black Jack!'
                time.sleep(0.5) 
                bank += int(bet) * 2
     
                            
        else: # if player don't have black jack
            if bank < bet: # if bank is lower than bet
                hit_or_stand(player) 
            else: #if bank is higher or equal to bet
                betx2 = hit_bet_stand(player)
                    
                if 'd' in betx2: #if player chose to double the bet amount
                    time.sleep(0.5) 
                    bank -= bet
                    time.sleep(0.5)     
                    bet *= 2
                    get_one_card(player)
                   
                    if not 's' in betx2:   #if player chose to hit 
                        hit_or_stand(player)   
            
                
            if points_amount(player) > MAX_POINTS: # if player reached more than 21 cap points. Busted.
                player_state = '    Bust!'
                dealer_state = '    Dealer win!'
                
            elif points_amount(dealer) == BLACKJACK_THRESHOLD:     # if player got more than 21 points or dealer has black jack
                dealer_state ='    Dealer win!    Black Jack!'
    
            else:     # if game is without black jacks and player has under 22 points.
                while points_amount(dealer) < DEALER_DRAW_THRESHOLD:     # if dealer has less than 17 points he will draw a card.
                    get_one_card(dealer)
                           
                if points_amount(dealer) > MAX_POINTS:       # if delear got more than 21 points he lost.          
                    player_state = '    You win!'
                    dealer_state = '    Bust!'
                    bank += int(bet) * 2
                    time.sleep(0.5) 
                
                else:       # if game were clean  player and dealer will compare the points amount.
                    if points_amount(player) > points_amount(dealer): # conditions for player to win
                        player_state = '    You win!'
                        bank += int(bet) * 2
                        time.sleep(0.5) 
                
                    elif points_amount(player) < points_amount(dealer): # conditions for dealer to win
                        dealer_state = '    Dealer win!'
                
                    else: # condition for equal score
                        player_state = '    Push!'
                        dealer_state = '    Push!'
                        bank += int(bet)
                        time.sleep(0.5) 
                      
        dealer_cards = 'unhidden' # after all've done their moves dealer also show his cards
        bet = 0
        clear()
        image()
        game_scores()
        input("\n\n\n\tPress enter to continue.")
        if not bank:
            print("Thank for playing Black Jack by Vladtsepesh.")
    game = input("To restart the game press Enter, to quit type 'q'.") #condition to restart or to quit the game

    
    


