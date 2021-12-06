class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

    def __str__(self):
        return self.name
