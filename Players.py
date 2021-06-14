class Players:
    def __init__(self, players):
        self.players = players
    
    def __add__(self, o):
        return Players(self.players + o)

    def __getitem__(self, item):
        return self.players[item]
    
    def __setitem__(self, item, o):
        self.players[item] = o