import random
from DeckOfCards import DeckOfCards
from Card import Card


class Player:

    def __init__(self, name: str, cards_num: int):
        """Constructor for the Player class.
         Initializes a player with a name ,start number of cards, and list of cards"""
        if type(name) != str or type(cards_num) != int:
            raise TypeError
        if 10 > cards_num or cards_num > 26:
            self.cards_num = 26
            self.name = name
            self.cards = []
        else:
            self.name = name
            self.cards_num = cards_num
            self.cards = []

    def __str__(self):
        """Returns the player's name ,number of cards he started with
         and player's hand in the end of game."""
        return f"{self.name} started with {self.cards_num} cards,\nand win the game with {len(self.cards)} cards.\n" \
               f"Winner hand: {self.cards}"

    def set_hand(self, new_deck):
        """Sets the player's hand by dealing a new card from the deck."""
        if type(new_deck) != DeckOfCards:
            raise TypeError
        else:
            for i in range(self.cards_num):
                new_card = new_deck.deal_one()
                self.cards.append(new_card)

    def get_card(self):
        """Gets a card from the player's hand and removes it from the hand."""
        if len(self.cards) == 0:
            raise IndexError("no more cards in hand!")
        else:
            lost_card = random.choice(self.cards)
            self.cards.remove(lost_card)
            return lost_card

    def add_card(self, card):
        """Adds a card to the player's hand."""
        if type(card) != Card:
            raise ValueError("card must be from type Card")
        else:
            self.cards.append(card)
