import sys
from itertools import permutations


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    for i in permutations(arr, m):
        print(' '.join(list(map(str, i))))


if __name__ == '__main__':
    main()
