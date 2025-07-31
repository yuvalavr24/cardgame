from unittest import TestCase
from Card import Card


class TestCard(TestCase):

    def setUp(self):
        self.new_card = Card(1, 4)
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_init_valid_card(self):
        # Check a creation of card is valid.
        self.assertEqual(str(self.new_card), "Ace of Club")

    def test_init_invalid_card_value(self):
        # Invalid case of creating a card with key for card_type_names(suits)
        # which not exist, should raise a KeyError.
        with self.assertRaises(KeyError):
            self.invalid_card = Card(13, 5)
        with self.assertRaises(KeyError):
            self.invalid_card = Card(13, 0)

    def test_init_invalid_card_suit(self):
        # Invalid case of creating a card with key for card_names(values)
        # which not exist, should raise a KeyError.
        with self.assertRaises(KeyError):
            self.invalid_card = Card(14, 4)
        with self.assertRaises(KeyError):
            self.invalid_card = Card(0, 4)

    def test_init_invalid_card_TypeError(self):
        # Invalid case of creating a card with value and suit
        # which are from type str, should raise a TypeError.
        with self.assertRaises(TypeError):
            self.invalid_card = Card("Ace", "Of Club")
        with self.assertRaises(TypeError):
            self.invalid_card = Card("3", "4")

    def test_greater_than_operator(self):
        card1 = Card(10, 1)
        card2 = Card(10, 2)
        card3 = Card(7, 4)
        # First case - higher value , should return True.
        self.assertTrue(card1 > card3)
        # Second case - same value and higher suit , should return True.
        self.assertTrue(card2 > card1)
        # Third case - higher value and lower suit , should return False.
        self.assertFalse(card1 > card2)
        # Fourth case - lower value , should return False.
        self.assertFalse(card3 > card1)

    def test_greater_than_operator_Ace(self):
        ace = Card(1, 4)
        card = Card(4, 1)
        # First case - self card is ace and the other is different , should return True.
        self.assertTrue(ace > card)
        # Second case - self card is not ace and the other is ace , should return False.
        self.assertFalse(card > ace)

    def test_equal_operator(self):
        card1 = Card(2, 3)
        card2 = Card(2, 1)
        card3 = Card(2, 3)
        # First case - same value but suit are different - should return False.
        self.assertFalse(card1 == card2)
        # Second case - same value and same suit(same card) - should return True.
        self.assertTrue(card1 == card3)
