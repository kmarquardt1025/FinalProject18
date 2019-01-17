from random import shuffle

suite = "H, D, S, C".split()
ranks = "2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A".split()

class deck:
    def __init__ (self,):
        self.deck = [(s,r) for s in suite for r in ranks ]
        print ("New deck created")

    def split(self):
        return (self.deck[:26],self.deck[26:])

    def shuffle(self):
        shuffle(self.deck)
        print("Deck shuffled")

class hand:
    def __init__(self,cards):
        self.cards = cards

    def add_card(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

    def __str__(self):
        return "Has {} cards left". format(len(self.name, drawn_card.))

class player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has played: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards (self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range 3:
                war_cards.append( self.cards.hand.pop())
                return war_cards

        def remaining_cards(self):
            return len(self.hand.cards) ! = 0






