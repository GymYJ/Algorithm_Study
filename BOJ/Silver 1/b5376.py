import sys
from math import gcd

t = int(sys.stdin.readline())
for _ in range(t):
    input_ = sys.stdin.readline().strip()
    bunja = 0
    idx = 2
    while True:
        if idx == len(input_):
            break
        if input_[idx] == '(':
            break
        bunja = bunja * 10 + int(input_[idx])
        idx += 1
    cnt = idx - 2
    cnt2 = 0
    if idx != len(input_):
        temp = bunja
        while True:
            idx += 1
            if input_[idx] == ')':
                break
            bunja = bunja * 10 + int(input_[idx])
            cnt2 += 1
        if bunja != temp:
            bunja = bunja - temp
    bunmo = 0
    while cnt2 > 0:
        bunmo = bunmo * 10 + 9
        cnt2 -= 1
    if bunmo == 0:
        bunmo = 1
    while cnt > 0:
        bunmo = bunmo * 10
        cnt -= 1
    gcd_ = gcd(bunja, bunmo)
    print(f'{bunja // gcd_}/{bunmo // gcd_}')
