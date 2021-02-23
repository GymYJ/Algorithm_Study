import sys
from itertools import combinations


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    arr = [i for i in range(1, n + 1)]
    for i in combinations(arr, m):
        print(' '.join(list(map(str, i))))


if __name__ == '__main__':
    main()
