
from Uno.Card import Card
from Uno.Deck import Deck

import random # shuffle deck if top card to play off of is a special card 
import sys


solutions = []


def display(l):
    '''display the solution'''
    for item in l:
        print(item)

def display2d(l):
    '''if no solution to dump all cards, display largest placement of cards'''
    max_cards = 0
    max_idx = 0
    for idx, sol in enumerate(l):
        if len(sol) > max_cards:
            max_cards = len(sol)
            max_idx = idx 

    print(f'Largest solution: {max_cards} cards')
    for card in l[max_idx]:
        print(f'({card}) ', end='')
    print('\n')


def find_solution(player_hand, discard_deck):
    '''
    1.) Start with the first card 
    2.) If all cards are placed -> return True
    3.) Try all cards.
        a.) if the card can be played, check if this card leads to solution
        b.) if placing card there leads to solution -> return True 
        c.) if placing card doesnt lead to solution, un play card and go back to (a)
    4.) if all cards have been tried and nothing worked return False 
    '''
    global solutions


    # Base condition: to exit recursion
    if len(player_hand) == 0:
        return True, discard_deck


    # get all available options of cards to place
    play_card = discard_deck[-1]
    playable_cards = []
    for card in player_hand:
        if card.is_compatable(play_card):
            playable_cards.append(card)

    for c in playable_cards:
        player_hand.remove(c)
        discard_deck.append(c)
        
        is_sol, deck = find_solution(player_hand, discard_deck)
        if is_sol == True:
            return True, deck

        else:
            # Backtrack
            solutions.append(list(discard_deck)) # save largest solution 
            player_hand.append(discard_deck.pop())

    return False,None


def main():
    if len(sys.argv) < 2:
        print('No command line arg was passed specifying the number random cards in hand, setting it to 10')
        card_num = 10
    else:
        try:
            card_num = int(sys.argv[1])
        except: 
            print('invalid argument, Need a number')
            return -1

    deck = Deck() # Creating a Deck of cards

    player_deck = []
    discard_deck = []

    # Drawing n random cards into players hand
    for i in range(card_num):
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
            solutions.append([card])
            break
    
    # DEBUG Display
    print(f'Card to play off of: {discard_deck[0]}')
    for idx, card in enumerate(player_deck):
        print(f'{idx}: {card}')


    is_sol, sol = find_solution(player_deck, discard_deck)

    if is_sol == True:
        print('\n' + '#' * 20 + '\n' + 'able to dump all cards')
        display(sol)

    else:
        print('\n' + '#' * 20 + 'no solution found')
        print('total solutions tried : ' + str(len(solutions)))
        display2d(solutions)
    

    return 0



if __name__ == '__main__':
    exit(main())



