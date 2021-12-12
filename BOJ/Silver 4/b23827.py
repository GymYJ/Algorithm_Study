import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
total = sum(arr) % 1000000007
answer = 0
for i in range(n):
    total -= arr[i]
    answer = (answer + arr[i] * total) % 1000000007
print(answer)
