import sys
from collections import defaultdict

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A_dic = defaultdict(int)
for i in range(n):
    num = 0
    for j in range(i, n):
        num += A[j]
        A_dic[num] += 1

answer = 0
for i in range(m):
    num = 0
    for j in range(i, m):
        num += B[j]
        if t - num in A_dic:
            answer += A_dic[t - num]
print(answer)
