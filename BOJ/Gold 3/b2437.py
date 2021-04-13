import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = 0
for i in range(n):
    if answer + 1 >= arr[i]:
        answer += arr[i]
    else:
        break
print(answer + 1)
