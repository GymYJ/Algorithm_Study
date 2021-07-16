import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n + 1)]
for i in permutations(arr, m):
    print(' '.join(map(str, list(i))))
