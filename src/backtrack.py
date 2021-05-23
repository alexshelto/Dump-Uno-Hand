
from Uno.Card import Card
from Uno.Deck import Deck

import random



best_solution = []

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
    print(f'length of player_hand: {len(player_hand)}')
    global best_solution

    for card in player_hand:
       if card.is_compatable(discard_deck[-1]):
           discard_deck.append(card)

           tmp = player_hand
           tmp.remove(card)
           is_sol, sol = find_solution(tmp, discard_deck)
           if is_sol == True:
               return True, sol

           # Else backtrack
           if len(discard_deck) >= len(best_solution):
               print('overwriting best solution')
               best_solution = discard_deck
               print(best_solution)

           discard_deck.pop()

    return False, best_solution



def main():
    deck = Deck() # Creating a Deck of cards

    player_deck = []
    discard_deck = []
    best = []

    # Drawing n random cards into players hand
    for i in range(10):
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
    if is_sol == False:
        print('No solution to dump all uno cards')
        print('biggest solution')
        for i in best_solution:
            print(i)
    else:
        print('it is possible')
        for i in best_solution:
            print(i)







if __name__ == '__main__':
    exit(main())
