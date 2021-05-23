
from Uno.Card import Card
from Uno.Deck import Deck

import random


solutions = []
biggest_sol = 0



def display(l):
    for item in l:
        print(item)

def display2d(l):
    max_cards = 0
    max_idx = 0
    for idx, sol in enumerate(l):
        if len(sol) > max_cards:
            max_cards = len(sol)
            max_idx = idx 

    if max_cards == 1:
        print(l[max_idx])

    for card in l[max_idx]:
        print(f'({card}) ', end='')
    print('\n')


'''
1.) Start with the first card 
2.) If all cards are placed -> return True
3.) Try all cards.
    a.) if the card can be played, check if this card leads to solution
    b.) if placing card there leads to solution -> return True 
    c.) if placing card doesnt lead to solution, un play card and go back to (a)
4.) if all cards have been tried and nothing worked return False 
'''
def find_solution(player_hand, discard_deck):
    global solutions

    # Break condition, if no cards left to place 
    if len(player_hand) == 0:
        return True
     
    for card in player_hand:
        if card.is_compatable(discard_deck[-1]):
            discard_deck.append(card)

            tmp = player_hand
            tmp.remove(card)

            # trying next step 
            is_sol, deck = find_solution(tmp, discard_deck)
            if is_sol == True: 
                return True, deck

            else:
                solutions.append(list(discard_deck))
                player_hand.append(discard_deck.pop())


    return False, None




def main():
    deck = Deck() # Creating a Deck of cards

    player_deck = []
    discard_deck = []

    # Drawing n random cards into players hand
    for i in range(5):
        player_deck.append(deck.draw_card())

    # Creating a discard card to play off of
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


    is_sol, sol = find_solution(player_deck, discard_deck)
    if is_sol == True:
        print('able to dump all cards')
        display(i)

    else:
        print('no solution found')
        print('total solutions tried : ' + str(len(solutions)))
        display2d(solutions)
    

    return 0




if __name__ == '__main__':
    exit(main())
