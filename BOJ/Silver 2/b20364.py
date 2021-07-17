import sys

n, q = map(int, sys.stdin.readline().split())
check = {}
for _ in range(q):
    ground = int(sys.stdin.readline())
    num = ground
    is_p = True
    others = 1
    while num > 1:
        if check.get(num):
            is_p = False
            others = num
        num = num // 2
    if is_p:
        check[ground] = 1
        print(0)
    else:
        print(others)
