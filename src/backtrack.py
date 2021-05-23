
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

    print(f'ph: {len(player_hand)} | dd: {len(discard_deck)}')

    # Break condition, if no cards left to place 
    if len(player_hand) == 0:
        return True
     
    # get compatable cards
    play_card = discard_deck[-1]
    for card in player_hand:
        moves = []
        if card.is_compatable(play_card):
            print(f'compatable: {card} | {play_card}')
            moves.append(card)
        else:
            print(f'Not compatable: {card} | {play_card}')
        print('#' * 20)

    for i in moves:
        print(i)

    '''
    for card in player_hand:
        if card.is_compatable(discard_deck[-1]):
            print(f'compatable: {card} | {discard_deck[-1]}')
            discard_deck.append(card)

            tmp = player_hand
            tmp.remove(card)

            # trying next step 
            is_sol, deck = find_solution(tmp, discard_deck)
            if is_sol == True: 
                return True, deck

            else:
                solutions.append(list(discard_deck))
                print("SOLUTION DIDNT WORK, BACKTRACKING")
                if len(discard_deck) > 2:
                    print(discard_deck[1])
                print(f'ph: {len(player_hand)} | dd: {len(discard_deck)}')

                player_hand.append(discard_deck.pop())
                print(f'ph: {len(player_hand)} | dd: {len(discard_deck)}')

        else:
            print(f'not compatable: {card} | {discard_deck[-1]}')
    '''


    return False, None


'''
Card to play off of: Color: yellow | Number: 9
0: Color: red | Number: 5
1: Color: yellow | Number: 5
2: Color: red | Number: 1
3: Color: green | Number: 1
4: Color: yellow | Number: 6


y9, y6, y5, r5, r1, g1 
    def __init__(self, color=None, number=None, special=None):
'''

def main():
    deck = Deck() # Creating a Deck of cards

    player_deck = []
    discard_deck = []

    # Drawing n random cards into players hand
    '''
    for i in range(5):
        player_deck.append(deck.draw_card())
    '''
    player_deck.append(Card('red', '5', None))
    player_deck.append(Card('yellow', '5', None))
    player_deck.append(Card('red', '1', None))
    player_deck.append(Card('green', '1', None))
    player_deck.append(Card('yellow', '6', None))

    '''
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
    '''
    dcard = Card('yellow', '9', None)
    #solutions.append(dcard)
    discard_deck.append(dcard)
    
    # DEBUG Display
    print(f'Card to play off of: {discard_deck[0]}')
    for idx, card in enumerate(player_deck):
        print(f'{idx}: {card}')


    is_sol, sol = find_solution(player_deck, discard_deck)
    '''
    if is_sol == True:
        print('\n' + '#' * 20 + 'able to dump all cards')
        display(i)

    else:
        print('\n' + '#' * 20 + 'no solution found')
        print('total solutions tried : ' + str(len(solutions)))
        display2d(solutions)
    

    return 0
    '''




if __name__ == '__main__':
    exit(main())
