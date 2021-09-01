import sys
from math import ceil

n, init_atk = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
low = 1
high = 123456000000000000
answer = 0
while low <= high:
    mid = (low + high) // 2
    hp = mid
    atk = init_atk
    is_p = True
    for t, a, h in arr:
        if t == 1:
            hp -= a * (ceil(h / atk) - 1)
            if hp <= 0:
                is_p = False
                break
        else:
            atk += a
            hp = min(mid, hp + h)
    if is_p:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
print(answer)
