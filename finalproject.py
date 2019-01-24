from random import shuffle

suite = "H, D, S, C".split()
ranks = "2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A".split()

class deck:
    """Class describing the entire deck of 52 cards"""
    def __init__ (self,):
        """Creates the actual deck of cards with the correct values and suites"""
        self.deck = [(s,r) for s in suite for r in ranks ]
        print ("New deck created...")

    def split(self):
        """Splits the deck into 2 halves"""
        return (self.deck[:26],self.deck[26:])

    def shuffle(self):
        """Shuffles the deck into a random order"""
        shuffle(self.deck)
        print("Deck shuffled...")

class hand:
    """Class describing each players hand"""
    def __init__(self,cards):
        """Defines each players hand of cards"""
        self.cards = cards

    def add_card(self, added_cards):
        """Function for adding cards to each hand"""
        self.cards.extend(added_cards)

    def remove_card(self):
        """Function for removing cards from each hand"""
        return self.cards.pop()

    def __str__(self):
        """Function to tell each player the score/ how many cards they have left"""
        return "Has {} cards left". format(len(self.name, drawn_card))

class Player:
    """Class describing the player of the game I.e you!"""
    def __init__(self, hand, name):
        """Creates variables for the player"""
        self.hand = hand
        self.name = name

    def play_card(self):
        """Function that removes a card from each hand and tells what cards were played by each party"""
        drawn_card = self.hand.remove_card()
        print("{} has played: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards (self):
        """Function comparing and then removing the cards from each respective party"""
        war_cards = []
        if len(self.hand.cards) < (3):
            return war_cards
        else:
            for x in range (3):
                war_cards.append(self.hand.cards.pop())
                return war_cards

    def cards_remaining(self):
        """Function that keeps track of how many cards are remaining"""
        return len(self.hand.cards) != 0

print("Welcome to War!")
print("In this game you will randomly draw cards from a shuffled deck to 'wage war'")
print("against a UNSC Strategic Artifical Intelligence Construct named Cortana.")
print("Are you ready to wage war?")
#Introduces the player to the game and gives them a brief set of rules

d = deck()
d.shuffle()
split1, split2 = d.split()
#Runs the functions to create the decks and then split and shuffle them


ai = Player(hand(split1),"Cortana")
name = input("Enter Your Name: ")
user = Player(hand(split2),name)
#Defines the names of the players and their corresponding variables

total_rounds = 0
number_of_war= 0
double_war =0
except_count =0
#Sets all of the counters to 0 to start the game

while user.cards_remaining() and ai.cards_remaining():
    total_rounds += 1
    print(" Get ready for a new round!")
    print("Current score:")
    print(user.name+" has "+str(len(user.hand.cards))+" cards left")
    print(ai.name+" has "+str(len(ai.hand.cards))+" cards left")
    print("Your card will now be played for you")
    print("")
#Introduces the player to each new round

    cards_in_play = []
    ai_card = ai.play_card()
    player_card = user.play_card()
    cards_in_play.append(ai_card)
    cards_in_play.append(player_card)
#Runs the functions that chooses cards from each party and compares them

    if ai_card[1] == player_card[1]:
        number_of_war +=1
        print(ai_card[1])
        print("Commencing war!")
        cards_in_play.extend(user.remove_war_cards())
        cards_in_play.extend(ai.remove_war_cards())
#Defines when to have a war to break a tie
        try:
            ai_card = ai.play_card()
            player_card = user.play_card()

            cards_in_play.append(ai_card)
            cards_in_play.append(player_card)

            if ranks.index(ai_card[1]) < ranks.index(player_card[1]):
                user.hand.add_card(cards_in_play)
#Defines when a normal war is won
            elif ranks.index(ai_card[1]) == ranks.index(player_card[1]):
                double_war +=1
                print("Wow you have engaged in a double war!")
                cards_in_play.extend(user.remove_war_cards())
                cards_in_play.extend(ai.remove_war_cards())
#Defines when there is a double war to break a tie in a normal war
                try:
                    ai_card = ai.play_card()
                    player_card = user.play_card()

                    cards_in_play.append(ai_card)
                    cards_in_play.append(player_card)
                    if ranks.index(ai_card[1]) < ranks.index(player_card[1]):
                        user.hand.add_card(cards_in_play)

                    else:
                        ai.hand.add_card(cards_in_play)
#Defines how a double war is won
                except:
                    except_count =+1
                    print("There are not enough cards for double war!")
                    break
            else:
                ai.hand.add_card(cards_in_play)
        except:
            except_count +=1
            print("There are not enough cards in the deck for a war! Game over!")
            break;
#Decides whether or not a war or double war is possible with the amount of cards remaining
    else:
        if ranks.index(ai_card[1]) < ranks.index(player_card[1]):
            user.hand.add_card(cards_in_play)
        else:
            ai.hand.add_card(cards_in_play)
if except_count>=1:
    if len(user.hand.cards)>len(ai.hand.cards):
        print(user.name+" has won this round of War!")
    else:
        print("Cortana has won this round of war!")
else:
    if len(user.hand.cards)==0:
        print("Game Over! Cortana has won this game of war!")
    else:
        print("Game Over! "+user.name+" has won this game of war!")
print("In this game, there were "+str(total_rounds)+" rounds!")
print("There were "+str(number_of_war)+" rounds of war in this game.")
print("There were "+str(double_war)+" rounds of double war in this game.")
print("Amount of war games that exceeded double war: "+str(except_count))
#List of if and else statements that determine who wins each round and who wins each game and provides a message for each respective condition







