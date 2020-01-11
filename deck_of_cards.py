import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} {self.suit}"


class Deck:
    def __init__(self):
        nums = ("A", "2", "3", "4", "5", "6", "7",
                "8", "9", "10", "J", "Q", "K")
        suits = ("♦", "♣", "♠", "♦")
        new_deck = [Card(suit, num) for num in nums for suit in suits]
        self.cards = new_deck

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        count = 0
        if num < self.count():
            num = self.count()
        if self.count() == 0:
            return ValueError("All cards have been dealt")
        while count < num:
            self.cards.pop()

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            return ValueError("Only full decks can be shuffled")
        else:
            return random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def deal_hand(self, num):
        count = 0
        hand = []
        while count < num:
            card = self.cards.pop()
            hand.append(card)
            count += 1
        return hand


my_deck = Deck()
print(my_deck)
print(my_deck.shuffle())
print(my_deck.deal_card())
print(my_deck.deal_hand(5))
print(my_deck)
