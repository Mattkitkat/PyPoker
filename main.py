from Deck import Deck
from Flop import Flop
from Turn import Turn
from River import River
from Player import Player
from Players import Players
from Community import Community
from Combinations import check_flush, check_two_pairs
import time

start_time = time.time()

max = 101
timeseen = 0
for deal in range(1, max):
    cards = Deck()
    
    players = Players([])

    for player in range(3):
        players = players + [Player([cards.deal()])]
    
    players[:] = [player + Player([cards.deal()]) for player in players]

    burn1 = cards.deal()
    flop = Flop([cards.deal(), cards.deal(), cards.deal()])
    burn2 = cards.deal()
    turn = Turn([cards.deal()])
    burn3 = cards.deal()
    river = River([cards.deal()])

    community = Community([]) + flop + turn + river

    players[:] = [player + community for player in players]

    n = 5
    winners = 0
    for player in players:
        result = player.evaluate()
        if(result):
            timeseen += 1

print(f'times flushes were dealt {timeseen} after this number of hands {max}')

print("--- %s seconds ---" % (time.time() - start_time))