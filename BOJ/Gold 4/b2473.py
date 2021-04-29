import sys
from itertools import combinations

n = int(sys.stdin.readline())
n_list = [i for i in range(n)]
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = []
ans_value = sys.maxsize
for c in combinations(n_list, 2):
    temp = list(c)
    value = arr[temp[0]] + arr[temp[1]]
    low = 0
    high = n - 1
    index = 0
    find = False
    while low <= high:
        mid = (low + high) // 2
        t_value = arr[mid] + value
        if t_value < 0:
            low = mid + 1
        else:
            high = mid - 1
        if abs(t_value) < ans_value and mid not in temp:
            ans_value = abs(t_value)
            index = mid
            find = True
    if find:
        temp.append(index)
        answer = temp
    if ans_value == 0:
        break
answer.sort()
answer = [arr[i] for i in answer]
print(' '.join(list(map(str, answer))))
