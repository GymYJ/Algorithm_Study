import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
min_value = sys.maxsize
answer = []
for i in range(n - 1):
    if min_value == 0:
        break
    low = i + 1
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        mix_value = arr[i] + arr[mid]
        if min_value > abs(mix_value):
            min_value = abs(mix_value)
            answer = [i, mid]
        if mix_value < 0:
            low = mid + 1
        else:
            high = mid - 1
print(arr[answer[0]], arr[answer[1]])
