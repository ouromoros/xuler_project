def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))

if __name__ == "__main__":
    n = 1
    while True:
        flag = True
        for i in range(2, 7):
            if not same_digits(n, n * i):
                n = n + 1
                flag = False
                break
        if flag:
            print(n)
            break
        else:
            n += 1
