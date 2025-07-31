class Card:

    def __init__(self, value: int, suit: int):
        """Constructor for the Card class."""
        if type(value) != int or type(suit) != int:
            raise TypeError("value and suit must be from type int")
        if value > 13 or value < 1:
            raise KeyError("Invalid value")
        else:
            self.value = value
        if suit > 4 or suit < 1:
            raise KeyError("Invalid suit")
        else:
            self.suit = suit

    def __repr__(self):
        """Returns a string representation of the card."""
        card_names = {
            1: "Ace",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        card_type_names = {
            1: "Diamond",
            2: "Spade",
            3: "Heart",
            4: "Club"
        }

        return f"{card_names[self.value]} of {card_type_names[self.suit]}"

    def __gt__(self, other):
        """using the greater than (>) operator for comparing cards."""
        # case when self card is "Ace"(highest card) ,
        # and the other has lower card, return True
        if self.value == 1 and other.value > 1:
            return True
        # case when self card is lower from "Ace"  ,
        # and the other has "Ace", return False
        elif other.value == 1 and self.value > 1:
            return False
        elif self.value == other.value and self.suit > other.suit:
            return True
        elif self.value == other.value and self.suit < other.suit:
            return False
        elif self.value > other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        """using the equality (==) operator for comparing cards."""
        # case when the value is equal and the suit is same, return True
        if self.value == other.value and self.suit == other.suit:
            return True
