import sys


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    a, b = n, m
    for i in range(1, m):
        a = a * (n - i)
        b = b * i
    print(a // b)


if __name__ == '__main__':
    main()
