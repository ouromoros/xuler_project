def is_palindrome(n):
    s = str(n)
    return s[::-1] == s

if __name__ == "__main__":
    result = -1
    for i in range(100, 1000):
        for j in range(100, 1000):
            x = i * j
            if is_palindrome(x):
                result = max(x, result)
    print(result)
