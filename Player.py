from typing import Counter
from collections import OrderedDict


class Player:
    def __init__(self, cards):
        self.cards = cards
        self.ranks = [card.rank for card in self.cards]
        self.suits = [card.suit for card in self.cards]

    def __add__(self, o):
        return Player(self.cards + o.cards)

    def __getitem__(self, item):
        return self.cards[item]
    
    def __str__(self):
        return ', '.join([str(x) for x in self.cards])
    
    def evaluate(self):
        #FLUSH
        x = Counter(self.suits).most_common(1)
        if(x[0][1] == 5):
            return 1
        
        #STRAIGHT
        
