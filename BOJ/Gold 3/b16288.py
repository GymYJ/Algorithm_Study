import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 'YES'
passport = [0 for _ in range(k)]
for now in arr:
    is_p = False
    for i, num in enumerate(passport):
        if now > num:
            passport[i] = now
            is_p = True
            break
    if not is_p:
        answer = 'NO'
        break
print(answer)
