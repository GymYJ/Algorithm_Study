import sys
import copy
from itertools import combinations
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = []
    area = []
    virus = []
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            if temp[j] == 0:
                area.append((i, j))
            elif temp[j] == 2:
                virus.append((i, j))
        arr.append(temp)
    max_area = 0
    for w in combinations(area, 3):
        cp_arr = copy.deepcopy(arr)
        for x, y in w:
            cp_arr[x][y] = 1
        x_list = [-1, 1, 0, 0]
        y_list = [0, 0, -1, 1]
        q = deque(virus)
        while q:
            now_x, now_y = q.popleft()
            for i, j in zip(x_list, y_list):
                x, y = now_x + i, now_y + j
                if 0 <= x < n and 0 <= y < m and cp_arr[x][y] == 0:
                    q.append((x,y))
                    cp_arr[x][y] = 2
        count_area = sum(i.count(0) for i in cp_arr)
        if max_area < count_area:
            max_area = count_area
    print(max_area)


if __name__ == '__main__':
    main()
