import enum
import functools
from collections import Counter

class Hand:
    class HandType(enum.IntEnum):
        HIGH_CARD = 0
        ONE_PAIR = 1
        TWO_PAIR = 2
        THREE_OF_A_KIND = 3
        STRAIGHT = 4
        FLUSH = 5
        FULL_HOUSE = 6
        FOUR_OF_A_KIND = 7
        STRAIGHT_FLUSH = 8
        ROYAL_FLUSH = 9

    @staticmethod
    def look(cards):
        same_suit = functools.reduce(lambda x, y: x and y,
            (c[0] == cards[0][0] for c in cards))
        count = Counter(c[0] for c in cards)
        if count == 2:
            # FULL_HOUSE or FOUR_OF_A_KIND
        elif count == 3:
            # three
        return None, None
    
    @staticmethod
    def num_map(n):
        m = {'J': 11, 'Q':12, 'K':13, 'A':14}
        return int(n) if n.isdigit() else m[n]

    def __init__(self, cards):
        parsed = [(self.num_map(c[:-1]), c[-1]) for c in cards]
        self.type, self.others = self.look(parsed)

    def __lt__(self, other):
        return (self.type, self.others) < (other.type, other.others)

    def __gt__(self, other):
        return (self.type, self.others) > (other.type, other.others)

if __name__ == "__main__":
    f = open()
    count = 0
    for line in f:
        cards = line.split(' ')
        hand1 = Hand(cards[:5])
        hand2 = Hand(cards[5:])
        if hand1 > hand2:
            count += 1
    print(count)
