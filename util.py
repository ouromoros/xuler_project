import array
import math

def Sieve(n):
    barr = array.array('b', (False for _ in range(n + 1)))
    # barr = [False for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if barr[i]: continue
        c = i * i
        while c < n:
            barr[c] = True
            c += i
    result = []
    for i in range(2, n + 1):
        if not barr[i]:
            result.append(i)
    return result
