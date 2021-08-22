import sys

n = int(sys.stdin.readline())
answer = 0
for i in range(1, n + 1):
    answer += i
print(answer)
