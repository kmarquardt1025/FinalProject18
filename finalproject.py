from random import shuffle

suite = "H, D, S, C".split()
ranks = "2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A"

class deck:
    def __init__ (self,):
        self.deck




    def facecard(self):
        face_cards = [11, 12, 13]
        for face_card in face_cards:
            if self.rank == face_card:
                return true
            else:
                return false

    def description(self):
        rank = self.value
        if rank == 1:
            rank = "Ace"
        elif rank == 11:
            rank = "Jack"
        elif rank == 12:
            rank = "Queen"
        elif rank == 13:
            rank = "King"

        return "{rank} of {self.suit}




