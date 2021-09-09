import sys
from math import gcd

n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
visit = [0 for _ in range(n + 1)]
answer = 1
for i in range(1, n + 1):
    if visit[i] == 0:
        visit[i] = 1
        count = 1
        now = arr[i]
        while now != i:
            visit[now] = 1
            count += 1
            now = arr[now]
        answer = answer * count // gcd(answer, count)
print(answer)
