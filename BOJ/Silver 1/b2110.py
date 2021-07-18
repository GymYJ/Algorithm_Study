import sys

n, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
low = 1
high = 1000000000
answer = 1000000000
while low <= high:
    mid = (low + high) // 2
    count = 1
    before = arr[0]
    length = 0
    for now in arr[1:]:
        length += now - before
        before = now
        if length >= mid:
            count += 1
            length = 0
    if count >= c:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
print(answer)
