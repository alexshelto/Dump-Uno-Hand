

from Deck import Deck
from Card import Card
from Player import Player
from Turn import Turn

import random

class Uno_Game:
    def __init__(self, players):
        '''players is a list of all of the players in the game
        generates a deck for the players'''
        self.deck = Deck()
        self.discard_deck = [] #TODO: maybe make this a deck as well
        self.players = players
        self.turn = Turn(len(players) - 1)
        #self.next_color = None #used to see compatable cards after a wild card is placed
        


    def deal_cards(self):
        '''Function to deal cards to players'''
        # Dealing 7 cards to each player
        #for i in range(7):
        for i in range(3):
            for player in self.players:
                player.draw(self.deck)

        # Placing a card on the top of the discard pile
        while True:
            card = self.deck.draw_card()
            # Only making a top card that is not a special card such as a reverse or a wild card
            if card.special != None:
                self.deck.cards.append(card)
                random.shuffle(self.deck.cards)
            else:
                self.discard_deck.append(card)
                self.next_color = card.color
                break


    def play_card(self, player, card):
        '''applys players desired card to the deck and updates the rule'''
        self.discard_deck.append(card)
        player.hand.remove(card)

        self.turn.apply_card(card)

        

    def show_players_hands(self):
        '''debug that shows each players hands and the amount of remaining cards'''
        for player in self.players:
            player.show_hand()

        print(f'Card to play off of: {self.discard_deck[-1]}')
        print(f'Remaining cards in deck: {len(self.deck.cards)}')



    def play_game(self):
        '''main game loop'''

        # 2 - 10 player game
        if len(self.players) < 2 or len(self.players) > 10: 
            exit(-1)

        self.deal_cards() #dealing cards to the players
        self.show_players_hands() #debug


        # While nobody has placed their last card (has 0 cards) handle turns
        while True:
            # Getting the next player
            turn = self.turn.next_player()
            current_player = self.players[turn]
            print(f'Current player: {current_player.name}')

            # output players hand
            print('checking current players hand for eligibility')
            top_card = self.discard_deck[-1]
            can_play = False

            for card in current_player.hand:
                if top_card.is_compatable(card) : #or card.color == self.next_color:
                    print(f'top card is: {top_card}... can play: {card}')
                    can_play = True


            # Current players desired choice
            # Play card then change turn to next player
            if can_play == True:
                desired_card = current_player.pick_card()
                # if desired card is wild or wild + 4, pick color
                if desired_card.special == 'wild' or desired_card.special == '+4_wild':
                    c = input('pick the color: ')
                    desired_card.color = c


                self.play_card(current_player, desired_card)

                if len(current_player.hand) == 0:
                    print('we have a winner')
                    break

                # Debug
                self.show_players_hands()

            # Draw card till an eligible card
            else:
                print('player could not play a card, drawing from deck')
                new_card = self.deck.draw_card()
                current_player.hand.append(new_card)
            








