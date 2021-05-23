
# Card Implementation for the uno cards

class Card:
    def __init__(self, color=None, number=None, special=None):
        self.color = color
        self.number = number
        self.special = special #includes skip, draw 2, wild card, reverse

    def __str__(self):
        '''outputs the card and its color if it has one'''
        if self.color is None:
            return self.special
        elif self.number is None:
            return f'Color: {self.color} | Number: {self.special}'
        else:
            return f'Color: {self.color} | Number: {self.number}'



    def same_color(self, other):
        '''returns true if two cards have the same color'''
        if self.color == other.color:
            return True
        else:
            return False

    def same_number(self, other):
        '''returns true if two cards have the same number'''
        if self.number == other.number:
            return True
        else:
            return False



    def is_compatable(self, other_card):
        '''checks if a card is compatable with another card,
           ie: if they have the same color or the same number'''
            # Note: add wild card functionality
        print(f'{self} | {other_card}')

        if self.same_color(other_card) and self.color != None:
            return True

        elif self.same_number(other_card) and self.number != None:
            return True

        # wild cards are compatable with any card
        elif (other_card.special == 'wild' or other_card.special == '+4_wild'
                or self.special == 'wild' or self.special == '+4_wild'):
            return True

        else:
            return False
