from unittest import TestCase
from unittest.mock import patch
from cardgame.card import Card
from cardgame.deck import DeckOfCards
from cardgame.player import Player


class TestPlayer(TestCase):

    def setUp(self):
        self.deck = DeckOfCards()
        self.player = Player("Napoleon Bonaparte", 20)
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_init_valid(self):
        # Testing the name, cards_num, cards of specific player initialize properly.
        self.assertEqual(self.player.name, "Napoleon Bonaparte")
        self.assertEqual(self.player.cards_num, 20)
        self.assertEqual(self.player.cards, [])

    def test_init_TypeError(self):
        # Testing the name, cards_num, cards when insert them wrong type of variables.
        with self.assertRaises(TypeError):
            self.player = Player(5, "Dani")

    def test_init_wrong_cards_num_low(self):
        # Testing extreme case cards_num lower than 10 turn auto to 26.
        self.new_player = Player("Dani", 5)
        self.assertEqual(self.new_player.cards_num, 26)

    def test_init_wrong_cards_num_high(self):
        # Testing extreme case cards_num higher than 26 turn auto to 26.
        self.new_player = Player("Dani", 28)
        self.assertEqual(self.new_player.cards_num, 26)

    def test_str_player_details(self):
        # Testing repr returns player details as expected.
        self.my_player = Player("Shalom", 20)
        self.assertEqual(str(self.my_player), "Shalom started with 20 cards,\nand win the game with 0 cards.\n"
                                              "Winner hand: []")

    def test_set_hand_valid(self):
        # Using mock for set_hand which calling to deal_one, and check if the cards were added to the player's hand.
        with patch("DeckOfCards.DeckOfCards.deal_one") as mock_set_hand:
            mock_card = Card(1, 4)
            mock_set_hand.return_value = mock_card
            self.player.set_hand(self.deck)
            mock_cards = []
            # Using for loop to add the same card 26 times, exactly like set_hand will do.
            for i in range(self.player.cards_num):
                mock_cards.append(mock_card)
            hand = self.player.cards
            # Check the cards in hand are equal to the mock_cards.
            self.assertEqual(hand, mock_cards)
            # Ensure that the len of the cards in hand is 26.
            self.assertEqual(len(hand), 20)

    def test_set_hand_TypeError_wrong_deck(self):
        # Calling wrong type of deck in set_hand raise TypeError.
        with self.assertRaises(TypeError):
            self.deck = ["Ace Of Club"]
            self.player.set_hand(self.deck)

    def test_add_card_valid(self):
        # Test that add_card method add the card to player hand.
        card = Card(3, 4)
        self.player.add_card(card)
        self.assertIn(card, self.player.cards)

    def test_add_card_invalid(self):
        # Case which add_card method get a card with different type from Card.
        with self.assertRaises(ValueError):
            card = "Ace of Club"
            self.player.add_card(card)

    def test_get_card_valid(self):
        # Test that get_card method remove card from player hand.
        delete_card = Card(4, 4)
        # Add the card.
        self.player.add_card(delete_card)
        # Check that the card in player hand.
        hand = self.player.cards
        self.assertEqual(hand, [delete_card])
        self.assertEqual(len(hand), 1)
        # Using get_card.
        self.player.get_card()
        # Check that the card is not in player hand anymore.
        self.assertNotIn(delete_card, self.player.cards)
        self.assertEqual(len(hand), 0)

    def test_get_card_IndexError_no_more_cards(self):
        # Testing extreme case which the player has no cards in hand, and get card try to get a card from his hand.
        self.new_player = Player("Yuval", 0)
        card1 = Card(2, 4)
        self.new_player.add_card(card1)
        with self.assertRaises(IndexError):
            for i in range(2):
                self.new_player.get_card()
