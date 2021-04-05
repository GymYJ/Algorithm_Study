import sys
from fractions import Fraction
from math import gcd


def xgcd(a, b):
    if b == 0:
        return [1, 0, a]
    x, y, d = xgcd(b, a % b)
    return [y, x - (a // b) * y, d]


def inv(a, M):
    x, y, d = xgcd(a, M)
    return x


m = int(sys.stdin.readline())
answer = 0
for _ in range(m):
    n, s = map(int, sys.stdin.readline().split())
    i = inv(n, 1000000007)
    answer = (answer + s * i) % 1000000007
print(answer)
