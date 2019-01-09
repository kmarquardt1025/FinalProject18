import random

'player1score' == 0
'player2score' == 0

class card:
    def __init__ (self, suit, value):
        self.suit = suit
        self.value = value

    def cardcolor (self):
        if self.suit == 'spades' or self.suit == 'clubs':
            return 'black'
        else:
            return 'red'

    def facecard(self):





