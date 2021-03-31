import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)
answer = 0
for i, num in enumerate(arr):
    left = i
    right = n - 1
    target = num * 0.9
    index = i
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            right = mid - 1
        else:
            index = mid
            left = mid + 1
    answer += index - i
print(answer)
