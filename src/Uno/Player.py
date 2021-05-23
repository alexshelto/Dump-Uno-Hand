
from Card import Card
from Deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        '''Shows all the cards in the players hand and how many cards they have'''
        for c in self.hand:
            print(c)
        print('#' * 30)
        print(f'Player: {self.name} has {len(self.hand)} cards')
        print('#' * 30 + '\n')

    def pick_card(self):
        '''Logic for a player to pick a card in their hand to play'''

        while True:
            for idx, card in enumerate(self.hand):
                print(f'{idx}: {card}')

            choice = input('pick a card to play: ')

            # ensuring the choice is in the cards
            if int(choice) >= 0 and int(choice) < len(self.hand):
                break
            else:
                print('You chose an invalid card, that doesnt exist in your hand')

        print(f'player chose: {self.hand[int(choice)]}')
        return self.hand[int(choice)]



