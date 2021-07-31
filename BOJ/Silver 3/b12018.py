import sys

n, m = map(int, sys.stdin.readline().split())
mini = []
for _ in range(n):
    P, L = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    temp.sort(reverse=True)
    if P < L:
        mini.append(1)
    else:
        temp = temp[:L]
        mini.append(temp[-1])
mini.sort()
answer = 0
for i in mini:
    if i <= m:
        answer += 1
        m -= i
    else:
        break
print(answer)
