from random import shuffle
from classes.Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def pop_card(self) -> Card | None:
        if (len(self.cards) > 0):
            return self.cards.pop()
