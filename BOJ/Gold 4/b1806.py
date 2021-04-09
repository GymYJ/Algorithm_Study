import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
left, right = 0, 0
answer = 100001
total = arr[0]
while True:
    if total >= s:
        if answer > right - left + 1:
            answer = right - left + 1
        if left < right:
            total -= arr[left]
            left += 1
        else:
            if right < n - 1:
                right += 1
                total += arr[right]
            else:
                break
    else:
        if right < n - 1:
            right += 1
            total += arr[right]
        else:
            break
print(answer if answer <= 100000 else 0)
