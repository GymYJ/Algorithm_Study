import sys
from collections import defaultdict


def dfs(now, lst, com, idx):
    if idx == len(lst):
        com[now] += 1
        return
    dfs(now, lst, com, idx + 1)
    dfs(now + lst[idx], lst, com, idx + 1)


n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr1 = arr[:n // 2]
arr2 = arr[n // 2:]
com1 = defaultdict(int)
com2 = defaultdict(int)
dfs(0, arr1, com1, 0)
dfs(0, arr2, com2, 0)
temp = []
for key in com1:
    temp.append((key, com1[key]))
temp.sort()
com1 = temp
temp = []
for key in com2:
    temp.append((key, com2[key]))
temp.sort()
com2 = temp
answer = 0
left, right = 0, len(com2) - 1
while left <= len(com1) - 1 and right >= 0:
    temp = com1[left][0] + com2[right][0]
    if temp == s:
        answer += com1[left][1] * com2[right][1]
        left += 1
        right -= 1
    elif temp < s:
        left += 1
    else:
        right -= 1
if s == 0:
    answer -= 1
print(answer)
