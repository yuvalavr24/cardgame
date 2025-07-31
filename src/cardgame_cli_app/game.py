from player import Player
from deck import DeckOfCards


class CardGame:

    def __init__(self, player1_name, player1_cards_num, player2_name, player2_cards_num):
        """Constructor for the CardGame class. Initializes a card game with players and a new deck. call to new_game"""
        self.deck = DeckOfCards()
        if type(player1_name) != str or type(player2_name) != str:
            raise TypeError("players names must be from type of str")
        if type(player1_cards_num) != int or type(player2_cards_num) != int:
            raise TypeError("cards_num must be from type of int")
        else:
            self.player1 = Player(player1_name, player1_cards_num)
            self.player2 = Player(player2_name, player2_cards_num)
            self.new_game()

    def new_game(self):
        """Starts a new game by shuffling the deck and dealing cards to players."""
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)

    def get_winner(self):
        """Determines the winner of the game based on the number of cards each player has."""
        if len(self.player1.cards) > len(self.player2.cards):
            return self.player1
        elif len(self.player2.cards) > len(self.player1.cards):
            return self.player2
        else:
            return None
