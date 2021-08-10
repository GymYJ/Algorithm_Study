import sys
from math import ceil

a, b, v = map(int, sys.stdin.readline().split())
one_day = a - b
days = ceil((v - a) / one_day)
print(days + 1)
