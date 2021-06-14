class Community:
    def __init__(self, cards):
        self.cards = cards

    def __add__(self, o):
        return Community(self.cards + o.cards)
    
    def __getitem__(self, item):
        return self.cards[item]