import sys

n = int(sys.stdin.readline())
n -= 1
answer = 1
while n > 0:
    n -= 6 * answer
    answer += 1
print(answer)
