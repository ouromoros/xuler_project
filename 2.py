N = 4e6

if __name__ == "__main__":
    a = 0
    b = 1
    s = 0
    while b <= N:
        if b % 2 == 0:
            s += b
        a, b = b, a + b
    print(s)
