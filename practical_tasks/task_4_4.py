import random


class Card():
    """
    This class represents a single card, with type and value."""

    def __init__(self, card_type, card_value):
        self.card_type = card_type
        self.card_value = card_value

    def representing(self):
        print("Type:", self.card_type)
        print("Value:", self.card_value)


class Deck(Card):
    """
     This class represents a single card deck (36 card). Deck has valid
    card values, card inside the deck are unique. Deck has methods to
    shuffle cards, to get card from the deck and to see current number
    of cards in the deck."""
    cards = []

    def __init__(self, card_type, card_value):
        super().__init__(card_type, card_value)

    def printing_cards(self):

        self.card = []
        for item in self.card_type:
            for value in self.card_value:
                self.card.append(item)
                self.card.append(value)
                self.cards.append(self.card.copy())
                self.card.clear()

        print("Deck:\n", self.cards)

    def shuffling_cards(self):
        for i in range(100):
            self.num = random.randint(0, len(self.cards) - 1)
            self.cards.append(self.cards.pop(self.num))
        print("\nShuffled deck:\n", self.cards)

    def getting_card(self):
        self.num = random.randint(0, len(self.cards) - 1)
        print("Card:", self.cards.pop(self.num))

    def number_of_cards(self):
        print(len(self.cards), "left")


a = Deck(['hearts', 'clovers', 'tiles', 'pikes'], ['ace', '6', '7', '8', '9', '10', 'jack', 'queen', 'king'])
a.printing_cards()
a.shuffling_cards()
for i in range(5):
    a.getting_card()
a.number_of_cards()

# b = Card(6, 'tiles')
# b.representing()
