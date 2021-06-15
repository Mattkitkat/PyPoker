from typing import Counter, Deque
from collections import OrderedDict, defaultdict
import bisect

class Player:
    straight = []
    straightFlush = []
    flush = []
    three = []
    two = []
    pair = [] 

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
        two_pair = False
        pair = False
        three_kind = False
        value_counts = defaultdict(lambda:0)

        ranks = []
        for card in self.cards:
            if card.rank not in ranks:
                ranks.append(card.rank)
                value_counts[card.rank] += 1
        
        suits = [card.suit for card in self.cards]
        
        #FLUSH
        x = Counter(suits).most_common(1)
        if(x[0][1] == 5):
            flush = True
        
        #STRAIGHT #todo enhance this primitive behavior 
        hand1 = ranks.copy()[:5]
        hand2 = ranks.copy()[1:6]
        hand3 = ranks.copy()[2:7]
        hands = [hand1, hand2, hand3]

        for hand in hands:
            if(len(hand) == 5):
                value_range = max(hand) - min(hand)
                if (value_range == 4):
                    straight = True

                if set(value_counts.values()) == set([3,1]):
                    three_kind = True
                
                if sorted(value_counts.values()) == [1,2,2]:
                    two_pair = True
                
                if 2 in value_counts.values():
                    pair = True

        if(straight and flush):
            self.straightFlush.append(self)
            return
        if(flush and not straight):
            self.flush.append(self)
            return
        if straight and not flush:
            self.straight.append(self)
            return
        if(three_kind):
            self.three.append(self)
            return
        if(two_pair):
            self.two.append(self)
            return
        if(pair):
            self.pair.append(self)
            return
