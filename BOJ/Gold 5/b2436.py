import sys
from math import gcd

a, b = map(int, sys.stdin.readline().split())
num = b // a
left, right = 1, num
min_value = left + right
answer = [left * a, right * a]
i = 2
while i * i <= num:
    if num % i == 0 and gcd(i, num // i) == 1:
        if min_value > i + num // i:
            min_value = i + num // i
            answer = [i * a, num // i * a]
    i += 1
answer.sort()
print(*answer)
