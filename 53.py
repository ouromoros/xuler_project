N = 100
if __name__ == "__main__":
    count = 0
    for n in range(0, N + 1):
        v = 1
        for i in range(1, n // 2):
            v *= n - i + 1
            v //= i
            if v > 1e6:
                count += n - i - i + 1
                break
    print(count)
