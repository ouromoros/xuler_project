N = 1000

if __name__ == '__main__':
    s = 0
    for i in range(1, N):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)
