import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = [0] * m
accu = 0
for a in arr:
    accu = (accu + a) % m
    count[accu] += 1
answer = count[0]
for i in range(m):
    answer += count[i] * (count[i] - 1) // 2
print(answer)
