import sys
from collections import deque

n, k, s = map(int, sys.stdin.readline().split())
back = []
front = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a < s:
        back.append([a, b])
    else:
        front.append([a, b])
back.sort()
front.sort()
back = deque(back)
answer = 0
while back:
    loc, stu = back[0]
    move = (s - loc) * 2
    total = 0
    while back and total < k:
        loc, stu = back.popleft()
        if total + stu <= k:
            total += stu
        else:
            stu = stu - (k - total)
            total = k
            back.appendleft([loc, stu])
    answer += move
while front:
    loc, stu = front[-1]
    move = (loc - s) * 2
    total = 0
    while front and total < k:
        loc, stu = front.pop()
        if total + stu <= k:
            total += stu
        else:
            stu = stu - (k - total)
            total = k
            front.append([loc, stu])
    answer += move
print(answer)
