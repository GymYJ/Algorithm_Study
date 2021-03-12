import sys
from collections import Counter


def main():
    n, m, inv = map(int, sys.stdin.readline().split())
    land = []
    for _ in range(n):
        land += map(int, sys.stdin.readline().split())

    block, length = sum(land) + inv, n * m
    land = dict(Counter(land))
    height, min_sec = 0, sys.maxsize

    for i in range(257):
        if length * i <= block:
            sec = 0
            for key in land:
                if key < i:
                    sec += (i - key) * land[key]
                elif key > i:
                    sec += (key - i) * 2 * land[key]
            if sec <= min_sec:
                min_sec = sec
                height = i

    print(min_sec, height)


if __name__ == '__main__':
    main()
