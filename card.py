import random
#pip install Sphinx
# .\make.bat html
class Card:
    """
    Represents a playing card.
    """
    def __init__(self, suit, number):
        """
        Initializes the card with a suit and number.
        """
        self._suit = suit
        self._number = number

    def __repr__(self):
        """
        Returns a string representation of the card.
        """
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """
        Gets or sets the card's suit.
        """
        return self._suit

    @suit.setter
    def suit(self, suit):
        """
        Sets the suit of the card.
        """
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("Invalid suit")

    @property
    def number(self):
        """
        Gets or sets the card's number.
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of the card.
        """
        valid = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("Invalid number")


class Deck:
    """
    Represents a deck of cards.
    """
    def __init__(self):
        """
        Initializes the deck and populates it with cards.
        """
        self._cards = []
        self.populate()

    def populate(self):
        """
        Fills the deck with 52 cards.
        """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        self._cards = [Card(s, n) for s in suits for n in numbers]

    def shuffle(self):
        """
        Shuffles the deck.
        """
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """
        Deals a number of cards from the deck.
        """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        """
        Returns the number of cards left in the deck.
        """
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"

deck = Deck()
print(deck)
