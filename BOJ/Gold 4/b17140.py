import sys
from collections import defaultdict

r, c, k = map(int, sys.stdin.readline().split())
answer = -1
row, col = 3, 3
arr = [[0 for _ in range(101)] for _ in range(101)]
for i in range(1, 4):
    temp = list(map(int, sys.stdin.readline().split()))
    for j, n in enumerate(temp, start=1):
        arr[i][j] = n
count = 0
for _ in range(101):
    if arr[r][c] == k:
        answer = count
        break
    if row >= col:
        for i in range(1, row + 1):
            counter = defaultdict(int)
            for j in arr[i][1:]:
                if j == 0:
                    continue
                counter[j] += 1
            dic = defaultdict(list)
            for j in counter:
                dic[counter[j]].append(j)
            counter = sorted(list(dic.keys()))
            index = 1
            for j in counter:
                temp = sorted(dic[j])
                for l in temp:
                    arr[i][index] = l
                    index += 1
                    arr[i][index] = j
                    index += 1
                if index > 100:
                    break
            col = max(col, index - 1)
            if index <= 100:
                while index <= 100:
                    arr[i][index] = 0
                    index += 1
    else:
        for i in range(1, col + 1):
            counter = defaultdict(int)
            for j in range(1, row + 1):
                if arr[j][i] == 0:
                    continue
                counter[arr[j][i]] += 1
            dic = defaultdict(list)
            for j in counter:
                dic[counter[j]].append(j)
            counter = sorted(list(dic.keys()))
            index = 1
            for j in counter:
                temp = sorted(dic[j])
                for l in temp:
                    arr[index][i] = l
                    index += 1
                    arr[index][i] = j
                    index += 1
                if index > 100:
                    break
            row = max(row, index - 1)
            if index <= 100:
                while index <= 100:
                    arr[index][i] = 0
                    index += 1
    count += 1
print(answer)
