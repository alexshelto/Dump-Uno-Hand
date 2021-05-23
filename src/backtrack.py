
from Uno.Card import Card
from Uno.Deck import Deck

import random


def main():
    deck = Deck() # Creating a Deck of cards

    player_deck = []
    discard_deck = []

    # Drawing n random cards into players hand
    for i in range(10):
        player_deck.append(deck.draw_card())

    # Placing a card on the top of a discard_deck
    while True:
        card = deck.draw_card()
        # Only making a top card that is not a special card such as a reverse or a wild card
        if card.special != None:
            deck.cards.append(card)
            random.shuffle(deck.cards)
        else:
            discard_deck.append(card)
            break
    
    # DEBUG Display
    print(f'Card to play off of: {discard_deck[0]}')
    for idx, card in enumerate(player_deck):
        print(f'{idx}: {card}')











if __name__ == '__main__':
    exit(main())
