from classes.Deck import Deck
from classes.Player import Player
from classes.Card import Card


class Game:
    def __init__(self):
        self.player1 = Player(input("First player name: "))
        self.player2 = Player(input("Second player name: "))
        self.deck = Deck()

    def wins(self, winner: Player):
        print(f"{winner} takes cards")

    def draw(self, player1_card: Card, player2_card: Card):
        print(f"{self.player1} puts {player1_card}, {self.player2} puts {player2_card}")

    def winner(self) -> str:
        if self.player1.wins > self.player2.wins:
            return str(self.player1)
        elif self.player2.wins > self.player1.wins:
            return str(self.player2)
        else:
            return "No one"

    def play(self):
        print("Let's go!")

        while len(self.deck.cards) >= 2:
            response = input(
                "Press X to exit. Press any other button to start the game.")
            if response == 'X':
                break

            player1_card = self.deck.pop_card()
            player2_card = self.deck.pop_card()
            self.draw(player1_card, player2_card)

            if player1_card > player2_card:
                self.player1.wins += 1
                self.wins(self.player1)
            else:
                self.player2.wins += 1
                self.wins(self.player2)

        print(f"Game over! {self.winner()} wins!")
