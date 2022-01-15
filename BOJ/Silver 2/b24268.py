import sys
from itertools import permutations

n, d = map(int, sys.stdin.readline().split())
arr = [i for i in range(d)]
find = False
answer = 0
for p in permutations(arr):
    if p[0] == 0:
        continue
    p = list(p)
    answer = 0
    mul = 1
    while p:
        answer += p.pop() * mul
        mul *= d
    if answer > n:
        find = True
        break
print(answer if find else -1)
