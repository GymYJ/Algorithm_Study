import sys
from collections import deque


def main():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0:
            break
        arr = []
        for _ in range(h):
            arr.append(list(map(int, sys.stdin.readline().split())))
        visit = [[0 for _ in range(w)] for _ in range(h)]
        x_list = [-1, -1, -1, 0, 0, 1, 1, 1]
        y_list = [-1, 0, 1, -1, 1, -1, 0, 1]
        count = 0
        for x in range(h):
            for y in range(w):
                if arr[x][y] == 1 and visit[x][y] == 0:
                    q = deque([(x, y)])
                    visit[x][y] = 1
                    while q:
                        now_x, now_y = q.popleft()
                        for a, b in zip(x_list, y_list):
                            next_x = now_x + a
                            next_y = now_y + b
                            if 0 <= next_x < h and 0 <= next_y < w and \
                                    arr[next_x][next_y] == 1 and visit[next_x][next_y] == 0:
                                visit[next_x][next_y] = 1
                                q.append((next_x, next_y))
                    count += 1
        print(count)


if __name__ == '__main__':
    main()
