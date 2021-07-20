import sys
from math import gcd, sqrt

n = int(input())
ns = list(int(sys.stdin.readline()) for _ in range(n))
ns.sort()
interval = []
ans = []

for i in range(1, n):
    interval.append(ns[i] - ns[i - 1])

prev = interval[0]
for i in range(1, len(interval)):
    prev = gcd(prev, interval[i])

for i in range(2, int(sqrt(prev)) + 1):  # 제곱근까지만 탐색
    if prev % i == 0:
        ans.append(i)
        ans.append(prev // i)
ans.append(prev)
ans = list(set(ans))  # 중복이 있을수 있으니 제거
ans.sort()
print(*ans)
