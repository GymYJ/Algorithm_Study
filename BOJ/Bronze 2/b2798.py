import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in combinations(arr, 3):
    if answer < sum(i) <= m:
        answer = sum(i)
        if answer == m:
            break
print(answer)
