import sys

n, k, l = map(int, sys.stdin.readline().split())
arr = [k, l]
arr.sort()
answer = 1
while arr[0] + 1 != arr[1] or arr[0] % 2 != 1:
    arr[0] = (arr[0] - 1) // 2 + 1
    arr[1] = (arr[1] - 1) // 2 + 1
    answer += 1
print(answer)
