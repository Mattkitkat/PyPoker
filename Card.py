class Card:
    rank = '';
    suit = '';

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}'
    
    def __getitem__(self, item):
        if item == 0:
            return self.rank
        if item == 1:
            return self.suit
        #todo: consider throw