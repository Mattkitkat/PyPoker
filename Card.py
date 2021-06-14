class Card:
    rank = 0;
    suit = '';

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def __gt__(self, o):
        return self.rank > o.rank
    
    def __ge__(self, o):
        return self.__gt__(o) or self.__eq__(o)

    def __lt__(self, o):
        return self.rank < o.rank

    def __le__(self, o):
        return self.__lt__(o) or self.__eq__(o)

    def __eq__(self, o):
        return self.rank == o.rank and self.suit == o.suit
    
    def __getitem__(self, item):
        if item == 0:
            return self.rank
        if item == 1:
            return self.suit
        #todo: consider throw