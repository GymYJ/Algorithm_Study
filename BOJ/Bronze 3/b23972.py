import sys
from math import ceil

k, n = map(int, sys.stdin.readline().split())
if n == 1:
    print(-1)
else:
    answer = ceil(k * n / (n - 1))
    if answer > (answer - k) * n:
        answer += 1
    print(answer)
