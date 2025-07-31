from unittest import TestCase
from DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck = DeckOfCards()
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_init(self):
        # Test that the deck contains 52 cards.
        self.assertEqual(len(self.deck.deck), 52)

    def test_repr(self):
        # Test repr returns a valid deck of difference cards, like should be in a real deck of cards.
        self.assertEqual(str(self.deck), "[Ace of Diamond, 2 of Diamond, 3 of Diamond, 4 of Diamond, 5 of Diamond,"
                                         " 6 of Diamond, 7 of Diamond, 8 of Diamond, 9 of Diamond, 10 of Diamond,"
                                         " Jack of Diamond, Queen of Diamond, King of Diamond, Ace of Spade,"
                                         " 2 of Spade, 3 of Spade, 4 of Spade, 5 of Spade, 6 of Spade, 7 of Spade,"
                                         " 8 of Spade, 9 of Spade, 10 of Spade, Jack of Spade, Queen of Spade,"
                                         " King of Spade, Ace of Heart, 2 of Heart, 3 of Heart, 4 of Heart,"
                                         " 5 of Heart, 6 of Heart, 7 of Heart, 8 of Heart, 9 of Heart,"
                                         " 10 of Heart, Jack of Heart, Queen of Heart, King of Heart,"
                                         " Ace of Club, 2 of Club, 3 of Club, 4 of Club, 5 of Club, 6 of Club,"
                                         " 7 of Club, 8 of Club, 9 of Club, 10 of Club, Jack of Club,"
                                         " Queen of Club, King of Club]")

    def test_shuffle(self):
        # Test that shuffling changes the order of cards.
        original_deck = self.deck.deck.copy()
        self.deck.cards_shuffle()
        shuffled_deck = self.deck.deck
        self.assertNotEqual(original_deck, shuffled_deck)

    def test_deal_one_valid(self):
        # Test that dealing one card reduces the deck size by one.
        original_size = len(self.deck.deck)
        card = self.deck.deal_one()
        new_size = len(self.deck.deck)
        self.assertEqual(new_size, original_size - 1)
        # Test that card is remove from the deck.
        self.assertNotIn(card, self.deck.deck)

    def test_deal_one_IndexError_no_more_cards(self):
        # Extreme case of dealing until end of cards(52 cards in deck).
        with self.assertRaises(IndexError):
            for i in range(56):
                self.deck.deal_one()
