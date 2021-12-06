class Card:
    suits = [
        "spades",
        "hearts",
        "diamonds",
        "clubs",
    ]

    values = [
        None, None, "2", "3",
        "4", "5", "6", "7",
        "8", "9", "10", "jack",
        "queen", "king", "ace",
    ]

    def __init__(self, value: int, suit: int):
        self.value = value
        self.suit = suit

    def __lt__(self, other: 'Card') -> bool:
        if self.value < other.value:
            return True
        if (self.value == other.value) and (self.suit < other.suit):
            return True
        return False

    def __gt__(self, other: 'Card') -> bool:
        if self.value > other.value:
            return True
        if (self.value == other.value) and (self.suit > other.suit):
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.values[self.value]} of {self.suits[self.suit]}"
