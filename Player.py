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
    fourKind = []
    fullHouse = []

    def __init__(self, cards):
        self.cards = []
        self.ranks = []
        self.suits = {}
        for card in cards:
            self.add_card_to_hand(card)

    def __getitem__(self, item):
        return self.cards[item]
    
    def __str__(self):
        return ', '.join([str(x) for x in self.cards])
    
    def add_card_to_hand(self, card):
        bisect.insort_left(self.cards, card)
        bisect.insort_left(self.ranks, card.rank)
        if(card.suit in self.suits):
            self.suits[card.suit] += 1
        else:
            self.suits[card.suit] = 1
    
    def __add__(self, o):
        return Player(self.cards + o.cards)

    def evaluate(self):
        straight = False
        flush = False
        two_pair = False
        pair = False
        three_kind = False
        four_kind = False
        full_house = False
        
        #FLUSH

        if(5 in self.suits.values()):
            flush = True
        
        hand1 = self.ranks[:5]
        hand2 = self.ranks[1:6]
        hand3 = self.ranks[2:7]

        hands = [hand1, hand2, hand3]
 
        for hand in hands:
            if(len(hand) == 5):
                #STRAIGHT
                value_range = max(hand) - min(hand)
                if (value_range == 4):
                    straight = True

                value_counts = defaultdict(lambda:0)
                for rank in hand:
                    value_counts[rank] += 1

                #Four of a kind
                if sorted(value_counts.values()) == [1,4]:
                    four_kind = True

                #Full house
                if sorted(value_counts.values()) == [2,3]:
                    full_house = True
                
                #Three of a kind
                if set(value_counts.values()) == set([3,1]):
                    three_kind = True
                
                #Two pair
                if sorted(value_counts.values()) == [1,2,2]:
                    two_pair = True
                
                #Pair
                if 2 in value_counts.values():
                    pair = True

        #todo royal flush missing
        if(straight and flush):
            self.straightFlush.append(True)
            return
        if(four_kind):
            self.fourKind.append(True)
            return
        if(full_house):
            self.fullHouse.append(True)
            return
        if(flush and not straight):
            self.flush.append(True)
            return
        if straight and not flush:
            self.straight.append(True)
            return
        if(three_kind):
            self.three.append(True)
            return
        if(two_pair):
            self.two.append(True)
            return
        if(pair):
            self.pair.append(True)
            return
