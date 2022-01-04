import sys

n, k = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
left, right = 1, 1
now = arr[1]
while left < n:
    if now == k:
        print(left, right)
        sys.exit()
    if now < k:
        right += 1
        if right > n:
            break
        now = now | arr[right]
    elif now > k:
        temp = arr[right]
        for i in range(right - 1, left - 1, -1):
            now = temp
            temp = temp | arr[i]
            if temp > k:
                left = i + 1
                break
        if now > k:
            left += 1
        if right < left:
            right = left
            if right > n:
                break
            now = arr[left]
print(-1)
