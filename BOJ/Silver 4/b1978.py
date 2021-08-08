import sys

check = [True] * 1001
prime = {}
for i in range(2, 1001):
    if check[i]:
        prime[i] = True
        for j in range(i, 1001, i):
            check[j] = False
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in arr:
    if prime.get(i):
        answer += 1
print(answer)
