from collections import defaultdict

def check_flush(hand):
    suits = [h[1] for h in hand]
    if len(set(suits)) == 1:
      return True
    else:
      return False


def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False