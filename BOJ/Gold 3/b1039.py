import sys
from collections import deque, defaultdict

n, k = sys.stdin.readline().split()
visit = defaultdict(list)
n = list(n)
m = len(n) - 1
k = int(k)
answer = 0
q = deque([[n, 0]])
while q:
    arr, c = q.popleft()
    num = int(''.join(arr))
    if c == k:
        answer = max(answer, num)
        continue
    for i in range(m):
        for j in range(i + 1, m + 1):
            cp = arr.copy()
            if i == 0 and cp[j] == '0':
                continue
            temp = cp[i]
            cp[i] = cp[j]
            cp[j] = temp
            num = int(''.join(cp))
            if c + 1 not in visit[num]:
                visit[num].append(c + 1)
                q.append([cp, c + 1])
print(answer if answer != 0 else -1)
