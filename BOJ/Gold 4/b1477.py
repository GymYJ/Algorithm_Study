import sys

n, m, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
dist = []
before = 0
for a in arr:
    dist.append(a - before)
    before = a
dist.append(l - before)
high = 1000
low = 1
answer = max(dist)
while low <= high:
    mid = (low + high) // 2
    count = 0
    for d in dist:
        count += (d - 1) // mid
    if count <= m:
        answer = min(answer, mid)
        high = mid - 1
    else:
        low = mid + 1
print(answer)
