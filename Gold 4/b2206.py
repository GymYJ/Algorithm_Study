import sys
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, list(input()))))
    visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1
    x_list = [-1, 1, 0, 0]
    y_list = [0, 0, -1, 1]
    q = deque([(0, 0, 1, 1)])
    while q:
        now_x, now_y, depth, crush = q.popleft()
        for x, y in zip(x_list, y_list):
            next_x = now_x + x
            next_y = now_y + y
            if 0 <= next_x < n and 0 <= next_y < m:
                if arr[next_x][next_y] == 1:
                    if crush and (visit[next_x][next_y][0] == 0 or visit[next_x][next_y][0] > depth + 1):
                        visit[next_x][next_y][0] = depth + 1
                        q.append((next_x, next_y, depth + 1, 0))
                else:
                    if crush:
                        if visit[next_x][next_y][1] == 0 or visit[next_x][next_y][1] > depth + 1:
                            visit[next_x][next_y][1] = depth + 1
                            q.append((next_x, next_y, depth + 1, crush))
                    else:
                        if visit[next_x][next_y][0] == 0 or visit[next_x][next_y][0] > depth + 1:
                            visit[next_x][next_y][0] = depth + 1
                            q.append((next_x, next_y, depth + 1, crush))
    if min(visit[n - 1][m - 1]) > 0:
        print(min(visit[n - 1][m - 1]))
    else:
        if max(visit[n - 1][m - 1]) > 0:
            print(max(visit[n - 1][m - 1]))
        else:
            print(-1)


if __name__ == '__main__':
    main()
