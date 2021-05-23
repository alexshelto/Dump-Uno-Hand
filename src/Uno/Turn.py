

# Turn class is functionality to determine whos turn it is in the game
# Keeps track after reverse cards are applied 

from Card import Card


class Turn:

    def __init__(self, player_count):
        self.pc = player_count #player count
        self.turn = 0 # Starts at the first player

        self.forward = True # counter clock wise movement, when True, increment +1 for turn, when false -1

    def apply_card(self, card):
        ''' applys the card to the game, if it is a reverse, the turn will count backwards'''
        if card.special == 'reverse':
            self.forward = not self.forward

        if card.special == 'skip': 
            increment = 2 # skip a player go to 2nd in line
        else:
            increment = 1 # Normal increment to next player

        if self.forward == True:
            self.turn += increment
            if self.turn > self.pc:
                self.turn = self.turn - self.pc
        else:
            self.turn -= increment
            if self.turn < 0:
                self.turn = self.turn + self.pc


    def next_player(self):
        return self.turn

