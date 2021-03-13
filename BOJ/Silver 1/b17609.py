import sys

t = int(sys.stdin.readline())
for _ in range(t):
    string = sys.stdin.readline().strip()
    size = len(string)
    half = size // 2
    left = 0
    right = size - 1
    lcount = 0
    lc = True
    while left <= right:
        if string[left] != string[right]:
            if string[left + 1] == string[right]:
                left += 1
                lcount += 1
            else:
                lcount = 2
        if lcount == 2:
            lc = False
            break
        left += 1
        right -= 1
    left = 0
    right = size - 1
    rcount = 0
    rc = True
    while left <= right:
        if string[left] != string[right]:
            if string[left] == string[right - 1]:
                right -= 1
                rcount += 1
            else:
                rcount = 2
        if rcount == 2:
            rc = False
            break
        left += 1
        right -= 1
    if not lc and not rc:
        print(2)
    elif lc or rc:
        count = lcount if lcount <= rcount else rcount
        if count == 1:
            print(1)
        else:
            print(0)
