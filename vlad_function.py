TWO_CARDS = 2

def result(hands, amount):
    if len(hands) == TWO_CARDS and hands.count('A'):
        return 'Black Jack'
    if amount > MAX_POINTS:
        return 'Bust'
    else:
        return str(amount)

def final_result(a, b):
    if a == b:
        a +='\tPush'
        b +='\tPush'
    elif a > b:
        a += '\tYou win!'
    
