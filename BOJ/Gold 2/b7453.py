import sys

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
ab = {}
for a in A:
    for b in B:
        if not ab.get(a + b):
            ab[a + b] = 1
        else:
            ab[a + b] += 1
answer = 0
for c in C:
    for d in D:
        if ab.get(-(c + d)):
            answer += ab[-(c + d)]
print(answer)
