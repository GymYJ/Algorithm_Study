import sys
from math import sqrt, inf
from collections import deque


def is_prime(n):
    root_n = int(sqrt(n))
    for i in range(2, root_n + 1):
        if n % i == 0:
            return False
    return True


t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    visit = [0 for _ in range(10000)]
    visit[a] = 1
    answer = inf
    q = deque([(a, 0)])
    while q:
        now, count = q.popleft()
        if answer <= count:
            continue
        if now == b:
            if answer > count:
                answer = count
            continue
        for i in range(4):
            for j in range(10):
                num = now // (10 ** (i + 1)) * 10 ** (i + 1) + (j * 10 ** i) + now % (10 ** i)
                if num >= 1000 and is_prime(num) and visit[num] == 0:
                    q.append((num, count + 1))
                    visit[num] = 1
    print(answer if answer != inf else 'Impossible')
