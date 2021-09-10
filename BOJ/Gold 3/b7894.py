import sys

t = int(sys.stdin.readline())
arr = [0] * 10000001
arr[1] = 1
now = 1
value = 1
for i in range(2, 10000001):
    now *= i
    while now >= 10:
        now = now / 10
        value += 1
    arr[i] = value
for _ in range(t):
    m = int(sys.stdin.readline())
    print(arr[m])

# 수학적 사고...
# import sys
# from math import log10
#
# def f(n):
#     ans=0
#     for i in range(2,n+1):
#         ans+=log10(i)
#     return int(ans)+1
#
# n=int(sys.stdin.readline())
# for i in range(n):
#     print(f(int(sys.stdin.readline())))
