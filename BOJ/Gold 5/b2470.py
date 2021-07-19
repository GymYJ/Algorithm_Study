import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = []
value = sys.maxsize
for i in range(0, n - 1):
    if arr[i] < 0:
        low = i + 1
        high = n - 1
        target = arr[i] * (-1)
        find = False
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                answer = [arr[i], arr[mid]]
                find = True
                break
            elif arr[mid] < target:
                low = mid + 1
                if value >= abs(arr[i] + arr[mid]):
                    value = abs(arr[i] + arr[mid])
                    answer = [arr[i], arr[mid]]
            else:
                high = mid - 1
                if value >= abs(arr[i] + arr[mid]):
                    value = abs(arr[i] + arr[mid])
                    answer = [arr[i], arr[mid]]
        if find:
            break
    else:
        if value >= abs(arr[i] + arr[i + 1]):
            answer = [arr[i], arr[i + 1]]
            break
print(answer[0], answer[1])
