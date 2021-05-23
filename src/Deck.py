# Card deck implementation

from Card import Card
import random 

'''
Card(color, number, special)

uno_deck_size = 108 # 108 cards in the uno deck
each deck includes eight "Skip" cards
eight "Reverse" cards
eight "Draw Two" cards,
four "Wild" cards,
and four "Wild Draw Four" cards.

Each color contains 19 cards, one number 0 card and two sets of cards numbered 1-9.
'''

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        '''builds a deck of cards then shuffles them'''
        for c in ['red', 'yellow', 'green', 'blue']:

            # Adding each colors reverse card, skip, and draw 2
            for i in range(2):
                self.cards.append(Card(color=c, special='reverse'))
                self.cards.append(Card(color=c, special='draw_2'))
                self.cards.append(Card(color=c, special='skip'))

            # Adding each number card 0-9, all have 2 cards per num besides 0
            for i in range(10): 
                self.cards.append(Card(color=c, number=i))
                if i != 0:
                    self.cards.append(Card(color=c, number=i))

            random.shuffle(self.cards) #shuffle after each color added to deck 

        # Adding the wild card and +4 wild card
        for i in range(4):
            self.cards.append(Card(special='wild'))
            self.cards.append(Card(special='+4_wild'))
                
        # Shuffle 
        random.shuffle(self.cards)

    
    def show(self):
        '''outputs all of the cards in the deck and the number of cards in the deck'''
        for c in self.cards:
            print(c)

        print(f'current deck size: {len(self.cards)}')

    def draw_card(self):
        '''drawing a card removes a card from the deck, then returns it
        later add functionality to check size? or infiniate place card feeds back into deck?'''
        return self.cards.pop()




