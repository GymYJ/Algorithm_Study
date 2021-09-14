import sys


def find(lst, x):
    lo = 0
    hi = len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid][0] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [(-1000000001, 0)]
dp2 = [0 for _ in range(n + 1)]
max_value = 0
for i, num in enumerate(arr[1:], start=1):
    if dp[-1][0] < num:
        dp.append((num, i))
        max_value += 1
        dp2[i] = max_value
    else:
        j = find(dp, num)
        dp2[i] = dp2[dp[j][1]]
        dp[j] = (num, i)
ans_list = []
value = len(dp) - 1
idx = n
while value > 0:
    if dp2[idx] == value:
        ans_list.append(arr[idx])
        value -= 1
    idx -= 1
ans_list.reverse()
print(len(dp) - 1)
print(*ans_list)
