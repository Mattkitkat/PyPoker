class Players:
    def __init__(self, players):
        self.players = players
    
    def __add__(self, o):
        return Players(self.players + o)

    def __getitem__(self, item):
        return self.players[item]

    def add_player(self, item):
        self.players.append(item)