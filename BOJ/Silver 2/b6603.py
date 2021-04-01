import sys
from itertools import combinations

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    k = arr[0]
    arr = arr[1:]
    arr.sort()
    for i in combinations(arr, 6):
        print(' '.join(list(map(str, i))))
    print()
