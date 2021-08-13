import sys

k, n = map(int, sys.stdin.readline().split())
arr = []
for _ in range(k):
    arr.append(int(sys.stdin.readline()))
low = 0
high = max(arr)
answer = 0
while low <= high:
    mid = (low + high) // 2
    if mid == 0:
        mid = 1
    count = 0
    for a in arr:
        count += a // mid
    if count >= n:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
print(answer)
