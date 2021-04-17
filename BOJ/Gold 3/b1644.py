import sys
from collections import deque

n = int(sys.stdin.readline())
prime = [True for _ in range(n + 1)]
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, n + 1, i):
            prime[j] = False
prime = [i for i in range(2, n + 1) if prime[i]]

answer = 0
total = 0
q = deque([])
for num in prime:
    total += num
    q.append(num)
    if total > n:
        while total > n:
            total -= q.popleft()
    if total == n:
        answer += 1
print(answer)
