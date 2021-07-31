import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
high = 60000000000
low = 0
minute = 0
while low <= high:
    mid = (high + low) // 2
    count = 0
    for i in arr:
        count += mid // i
        if mid % i != 0:
            count += 1
        if count >= n:
            break
    if count >= n:
        minute = mid
        high = mid - 1
    else:
        low = mid + 1
minute -= 1
candidate = []
for i, num in enumerate(arr, start=1):
    n -= minute // num
    if minute % num == 0:
        candidate.append(i)
    else:
        n -= 1
print(candidate[n - 1])
