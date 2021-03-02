import sys
import copy
from collections import deque

n = int(sys.stdin.readline())
move = [-1, 0, 1]
arr = list(map(int, sys.stdin.readline().split()))
max_dp = deque([copy.deepcopy(arr)])
min_dp = deque([copy.deepcopy(arr)])
for _ in range(n - 1):
    arr = list(map(int, sys.stdin.readline().split()))
    add_max = []
    add_min = []
    for j in range(3):
        max_temp = []
        min_temp = []
        for m in move:
            if 0 <= j + m < 3:
                max_temp.append(max_dp[0][j + m] + arr[j])
                min_temp.append(min_dp[0][j + m] + arr[j])
        add_max.append(max(max_temp))
        add_min.append(min(min_temp))
    max_dp.append(add_max)
    max_dp.popleft()
    min_dp.append(add_min)
    min_dp.popleft()
print(max(max_dp[0]), min(min_dp[0]))
