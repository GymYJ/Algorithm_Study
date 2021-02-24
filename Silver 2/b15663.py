import sys
from itertools import permutations


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    answer = set()
    for i in permutations(arr, m):
        if i not in answer:
            print(' '.join(list(map(str, i))))
            answer.add(i)


if __name__ == '__main__':
    main()
