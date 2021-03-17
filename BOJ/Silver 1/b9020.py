import sys
from math import sqrt


def check(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    small = n // 2
    big = small
    if check(small):
        print(small, big)
        continue
    while True:
        small -= 1
        big += 1
        if check(small) and check(big):
            print(small, big)
            break
