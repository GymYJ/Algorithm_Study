import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
low = 1
high = 1000000000
answer = 1000000000
while low <= high:
    mid = (low + high) // 2
    money = mid
    count = 1
    is_p = True
    for a in arr:
        if money >= a:
            money -= a
        else:
            money = mid
            if money < a:
                is_p = False
            money -= a
            count += 1
    if count > m or not is_p:
        low = mid + 1
    else:
        answer = mid
        high = mid - 1
print(answer)
