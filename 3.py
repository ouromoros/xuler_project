import math
from util import Sieve

N = 600851475143

if __name__ == "__main__":
    m = N
    for p in Sieve(int(math.sqrt(N))):
        if N % p == 0:
            m = p
    print(m)
        
