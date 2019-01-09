import random

'player1score' == 0
'player2score' == 0

def shuffle_cards():
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    random.shuffle_cards(deck)
    return deck

