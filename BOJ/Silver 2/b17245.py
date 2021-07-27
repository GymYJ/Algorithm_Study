import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr += list(map(int, sys.stdin.readline().split()))
total = sum(arr)
half = total // 2 if total % 2 == 0 else total // 2 + 1
answer = 10000000
left = 0
right = 10000000
while left <= right:
    mid = (left + right) // 2
    count = 0
    for computer in arr:
        if computer <= mid:
            count += computer
        else:
            count += mid
        if count >= half:
            break
    if count >= half:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
