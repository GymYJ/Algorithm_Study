import sys


def find(lst, x):
    lo = 0
    hi = len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [-1000000001]
for num in arr:
    if dp[-1] < num:
        dp.append(num)
    else:
        dp[find(dp, num)] = num
print(len(dp) - 1)
