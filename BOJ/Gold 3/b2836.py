import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: x[1])
answer = 0
now = 0
left, right = -1, -1
for a, b in arr:
    if left == -1 and right == -1:
        answer += a - now
        now = a
        if a < b:
            answer += b - now
            now = b
        else:
            left, right = b, a
    elif b <= right:
        right = max(right, a)
    else:
        answer += right - now
        answer += right - left
        now = left
        left, right = -1, -1
        if a < b:
            answer += b - now
            now = b
        else:
            left, right = b, a
if left != -1 and right != -1:
    answer += right - now
    answer += right - left
    now = left
answer += m - now
print(answer)
