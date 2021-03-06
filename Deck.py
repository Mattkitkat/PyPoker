import random
from typing import Deque
from Card import Card

class Deck:
    suits = ['H', 'C', 'S', 'D']
    ranks = 15

    def __init__(self) -> None:
        self.cards = []
        for suit in self.suits:
            for rank in range(2, self.ranks):
                #todo move this to repr
                # if(rank == 10):
                #     rank = 'T'
                # if(rank == 11):
                #     rank = 'J'
                # if(rank == 12):
                #     rank = 'Q'
                # if(rank == 13):
                #     rank = 'K'
                # if(rank == 14):
                #     rank = 'A'
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        random.shuffle(self.cards)

        self.slice_deck()
        self.cards = Deque(self.cards)
        
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return ', '.join(str(x) for x in reversed(self.cards))

    def deal(self):
        if(self.cards):
            return self.cards.pop()
    
    def slice_deck(self):
        randomness = random.uniform(-1, 1)
        hand1 = self.cards[0:int((len(self.cards)/2)+randomness)]
        hand2 = self.cards[int((len(self.cards)/2)+randomness):len(self.cards)]

        hand2.extend(hand1)
        self.cards = hand2