import sys

h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = []
low = 0
high = max(h, w)
for _ in range(k):
    temp = list(map(int, sys.stdin.readline().split()))
    low = max(low, temp[0])
    arr.append(temp[1])
arr.sort()
answer = high
while low <= high:
    mid = (low + high) // 2
    count = 0
    now = 0
    for a in arr:
        if a > now:
            now = a + mid - 1
            count += 1
            if count > n:
                break
    if count <= n:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
print(answer)
