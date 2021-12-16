import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
if m == 0:
    print(0)
    sys.exit()
arr.sort()
left, right = 0, 0
answer = 2000000000
while right < n:
    while left <= right:
        now = arr[right] - arr[left]
        if now >= m:
            if answer > now:
                answer = arr[right] - arr[left]
            left += 1
        else:
            break
    right += 1
print(answer)
