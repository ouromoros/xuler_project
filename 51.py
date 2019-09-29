from util import Sieve
from collections import Counter, defaultdict
from itertools import combinations

N = int(1e6)

if __name__ == "__main__":
    primes = Sieve(N)

    pmap = defaultdict(list)
    for p in primes:
        s = str(p)
        c = Counter(s)
        for k, v in c.items():
            positions = list(filter(lambda i: s[i] == k, range(len(s))))
            for m in range(1, 4):
                for pos in combinations(positions, m):
                    ns = ''.join('A' if i in pos else s[i] for i in range(len(s)))
                    pmap[ns].append(s)
    
    result = N
    for k, v in pmap.items():
        if len(v) >= 8:
            print(v)
            result = min(result, min(int(s) for s in v))
    print(result)
