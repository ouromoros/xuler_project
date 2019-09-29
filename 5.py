from util import Sieve

N = 20

if __name__ == "__main__":
    parr = Sieve(N)
    mpcount = [0 for _ in range(len(parr))]
    for n in range(1, N + 1):
        for i, p in enumerate(parr):
            count = 0
            if n == 1: break
            while n % p == 0:
                count += 1
                n /= p
            mpcount[i] = max(mpcount[i], count)
    result = 1
    for i, c in enumerate(mpcount):
        result *= parr[i]**c
    print(result)
