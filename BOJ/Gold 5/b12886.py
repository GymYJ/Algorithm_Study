import sys
from collections import deque


def change(i, j):
    if i < j:
        return i * 2, j - i
    return i - j, j * 2


a, b, c = map(int, sys.stdin.readline().split())
visit = set()
visit.add((a, b, c))
answer = 0
q = deque([(a, b, c)])
while q:
    a, b, c = q.popleft()
    if a == b and b == c:
        answer = 1
        break
    if a != b:
        na, nb = change(a, b)
        if (na, nb, c) not in visit:
            visit.add((na, nb, c))
            q.append((na, nb, c))
    if a != c:
        na, nc = change(a, c)
        if (na, b, nc) not in visit:
            visit.add((na, b, nc))
            q.append((na, b, nc))
    if b != c:
        nb, nc = change(b, c)
        if (a, nb, nc) not in visit:
            visit.add((a, nb, nc))
            q.append((a, nb, nc))
print(answer)
