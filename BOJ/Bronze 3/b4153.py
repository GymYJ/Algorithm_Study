import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    side = max(a, b, c)
    others = 0
    for n in [a, b, c]:
        if n == side:
            continue
        else:
            others += n ** 2
    if others == side ** 2:
        print('right')
    else:
        print('wrong')
