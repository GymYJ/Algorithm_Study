from math import gcd


def main():
    t = int(input())
    for _ in range(t):
        m, n, x, y = list(map(int, input().split()))
        i, j = 0, 0
        k = -1
        limit = m * n // gcd(m, n)
        a, b = x, y
        while a <= limit and b <= limit:
            a = m * i + x
            b = n * j + y
            if a == b:
                k = a
                break
            elif a < b:
                i += 1
            else:
                j += 1
        print(k)


if __name__ == '__main__':
    main()
