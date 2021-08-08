import sys

while True:
    try:
        x = int(input())
        x = x * 10000000
    except:
        break
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.sort()
    small = 0
    big = n - 1
    is_p = False
    while small < big:
        if arr[small] + arr[big] == x:
            is_p = True
            break
        if arr[small] + arr[big] > x:
            big -= 1
        else:
            small += 1
    if is_p:
        print('yes', arr[small], arr[big])
    else:
        print('danger')
