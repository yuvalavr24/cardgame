from Card import Card
import random


class DeckOfCards:

    def __init__(self):
        """Constructor for the DeckOfCards class. Initializes a deck of cards in a list."""
        self.deck = []
        for suit in range(1, 5):
            for value in range(1, 14):
                self.deck.append(Card(value, suit))

    def __repr__(self):
        """Returns a string representation of the deck of cards."""
        return str(self.deck)

    def cards_shuffle(self):
        """mixing the deck of cards."""
        random.shuffle(self.deck)

    def deal_one(self):
        """Deals one card from the deck and removes it from the deck."""
        if len(self.deck) != 0:
            new_card = random.choice(self.deck)
            self.deck.remove(new_card)
            return new_card
        else:
            raise IndexError("no more cards to deal")
