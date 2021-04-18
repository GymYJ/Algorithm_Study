import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
left, right = 0, k
answer = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)
    if count >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
