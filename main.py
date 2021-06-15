from Deck import Deck
from Flop import Flop
from Turn import Turn
from River import River
from Player import Player
from Players import Players
from Community import Community
import time

start_time = time.time()

max = 10001
#todo recheck propoer convention!
timeseenFlush = 0
timeseenStraight = 0
timeseenStraightFlush = 0
timeseenPair = 0
timeseenTwoPair = 0
timeseenThree = 0

for deal in range(1, max):
    cards = Deck()
    
    players = Players([])

    for player in range(3):
        x = Player([cards.deal()])
        players.add_player(x)

    for player in players:
        player.add_card_to_hand(cards.deal())

    burn1 = cards.deal()
    flop = Flop([cards.deal(), cards.deal(), cards.deal()])
    burn2 = cards.deal()
    turn = Turn([cards.deal()])
    burn3 = cards.deal()
    river = River([cards.deal()])

    community = Community([]) + flop + turn + river

    for player in players:
        for card in community:
            player.add_card_to_hand(card)

    n = 5
    winners = 0
    for player in players:
        result = player.evaluate()

#todo fix this len thing as its not ideal
print(f'times Flushes were dealt {len(players[0].flush)} after this number of hands {max}')
print(f'times Straights were dealt {len(players[0].straight)} after this number of hands {max}')
print(f'times StraightFlush were dealt {len(players[0].straightFlush)} after this number of hands {max}')
print(f'times Three of a kind were dealt {len(players[0].three)} after this number of hands {max}')
print(f'times Two Pairs were dealt {len(players[0].two)} after this number of hands {max}')
print(f'times Pairs were dealt {len(players[0].pair)} after this number of hands {max}')

print("--- %s seconds ---" % (time.time() - start_time))