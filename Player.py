from typing import Counter, Deque
from collections import OrderedDict
import bisect

class Player:
    def __init__(self, cards):
        self.cards = []
        for card in cards:
            self.add_card_to_hand(card)

    def __getitem__(self, item):
        return self.cards[item]
    
    def __str__(self):
        return ', '.join([str(x) for x in self.cards])
    
    def add_card_to_hand(self, card):
        bisect.insort_left(self.cards, card)
    
    def __add__(self, o):
        return Player(self.cards + o.cards)

    def evaluate(self):
        straight = False
        flush = False

        ranks = []
        for card in self.cards:
            if card.rank not in ranks:
                ranks.append(card.rank)
        
        suits = [card.suit for card in self.cards]
        
        #FLUSH
        x = Counter(suits).most_common(1)
        if(x[0][1] == 5):
            flush = True
        
        #STRAIGHT #todo enhance this primitive behavior 
        y = ranks.copy()[:5]
        value_range = max(y) - min(y)
        if (value_range==4):
            straight = True
        
        y = ranks.copy()[1:6]
        value_range = max(y) - min(y)
        if (value_range==4):
            straight = True

        y = ranks.copy()[2:7]
        value_range = max(y) - min(y)
        if (value_range==4):
            straight = True
        
        if(straight and flush):
            return 3
        if straight and not flush:
            return 2 
        if(flush and not straight):
            return 1
