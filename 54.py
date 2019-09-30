import enum
import functools
from collections import Counter

class HandType(enum.IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

class Hand:
    @staticmethod
    def look(cards):
        nums = list(c[0] for c in cards)
        num_count = Counter(nums)
        count = len(num_count)
        sorted_nums = list(num_count)
        # if the count equals, then sort by value
        sorted_nums.sort(key=lambda x: (num_count[x], x), reverse=True)
        big_count = num_count[sorted_nums[0]]

        if count == 2:
            # FULL_HOUSE, FOUR_OF_A_KIND
            if big_count == 3:
                type =  HandType.FULL_HOUSE
            else:
                type =  HandType.FOUR_OF_A_KIND
        elif count == 3:
            # Three_OF_A_KIND, TWO_PAIRS
            if big_count == 3:
                type = HandType.THREE_OF_A_KIND
            else:
                type = HandType.TWO_PAIRS
        elif count == 4:
            # ONE_PAIR
            type =  HandType.ONE_PAIR
        else:
            # ROYAL_FLUSH, STRAIGHT_FLUSH, HIGH_CARD, FLUSH
            is_straight = sorted_nums[0] - sorted_nums[4] == 4

            if is_straight:
                type = HandType.STRAIGHT
            else:
                type = HandType.HIGH_CARD
                
        same_suit = functools.reduce(lambda x, y: x and y,
            (c[1] == cards[0][1] for c in cards))

        # treat FLUSH specially at last because it overlaps with other type
        if same_suit:
            if is_straight and sorted_nums[0] == 14:
                type = HandType.ROYAL_FLUSH
            elif is_straight:
                type = HandType.STRAIGHT_FLUSH
            elif type < HandType.FLUSH:
                type = HandType.FLUSH
            
        return type, sorted_nums
    
    @staticmethod
    def num_map(n):
        m = {'T' : 10, 'J': 11, 'Q':12, 'K':13, 'A':14}
        return int(n) if n.isdigit() else m[n]

    def __init__(self, cards):
        parsed = [(self.num_map(c[0]), c[1]) for c in cards]
        self.type, self.others = self.look(parsed)

    def __lt__(self, other):
        return (self.type, self.others) < (other.type, other.others)

    def __gt__(self, other):
        return (self.type, self.others) > (other.type, other.others)

if __name__ == "__main__":
    f = open('data/p054_poker.txt')
    count = 0
    for line in f:
        cards = line.split(' ')
        hand1 = Hand(cards[:5])
        hand2 = Hand(cards[5:])
        if hand1 > hand2:
            count += 1
    print(count)
