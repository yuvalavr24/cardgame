from unittest import TestCase
from cardgame.game import CardGame


class TestCardGame(TestCase):

    def setUp(self):
        self.game = CardGame("Noa", 20, "Neta", 20)
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_new_game_valid(self):
        # Test that a new game initializes the players with the correct number of cards.
        cards_player1 = self.game.player1.cards
        cards_player2 = self.game.player2.cards
        self.assertEqual(len(cards_player1), 20)
        self.assertEqual(len(cards_player2), 20)

    def test_new_game_wrong_cards_num(self):
        # Testing cards_num lower than 10 or higher than 26 turn auto to 26.
        self.game = CardGame("Noa", 9, "Neta", 27)
        cards_player1 = self.game.player1.cards
        cards_player2 = self.game.player2.cards
        self.assertEqual(len(cards_player1), 26)
        self.assertEqual(len(cards_player2), 26)

    def test_new_game_TypeError_name(self):
        # Test that type of player name which is not str raise TypeError.
        with self.assertRaises(TypeError):
            self.game = CardGame(20, 20, 20, 20)

    def test_new_game_TypeError_cards_num(self):
        # Test that type of cards_num which is not int raise TypeError.
        with self.assertRaises(TypeError):
            self.game = CardGame("Noa", "20", "Neta", "20")

    def test_get_winner_tie(self):
        # Test that get_winner returns the correct winner based on the number of cards(both players 26 cards).
        self.assertIsNone(self.game.get_winner())

    def test_get_winner_player1_win(self):
        # Test that get_winner returns the details of the winner
        # based on the number of cards(one player has more cards).
        card = self.game.player2.get_card()
        self.game.player1.add_card(card)
        self.assertEqual(self.game.get_winner(), self.game.player1)
        self.assertEqual(len(self.game.player1.cards), 21)
        self.assertEqual(len(self.game.player2.cards), 19)

    def test_get_winner_player2_win(self):
        # Test that get_winner returns the details of the winner
        # based on the number of cards(second player has more cards).
        card = self.game.player1.get_card()
        self.game.player2.add_card(card)
        self.assertEqual(self.game.get_winner(), self.game.player2)
        self.assertEqual(len(self.game.player1.cards), 19)
        self.assertEqual(len(self.game.player2.cards), 21)
