class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def __getitem__(self, item):
        return self.cards[item]
    
    def __str__(self):
        return ', '.join([str(x) for x in self.cards])
    
    def __len__(self):
        return len(self.cards)
    
    def __add__(self, o):
        return Hand(self.cards + o.cards)