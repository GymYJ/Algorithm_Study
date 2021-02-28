import sys
from collections import deque


def main():
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    max_safe = 0
    x_list = [-1, 1, 0, 0]
    y_list = [0, 0, -1, 1]
    rain = 0
    while True:
        count = 0
        visit = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if arr[x][y] > rain and visit[x][y] == 0:
                    visit[x][y] = 1
                    q = deque([(x, y)])
                    while q:
                        now_x, now_y = q.popleft()
                        for a, b in zip(x_list, y_list):
                            next_x = now_x + a
                            next_y = now_y + b
                            if 0 <= next_x < n and 0 <= next_y < n and \
                                    visit[next_x][next_y] == 0 and arr[next_x][next_y] > rain:
                                visit[next_x][next_y] = 1
                                q.append((next_x, next_y))
                    count += 1
        if max_safe < count:
            max_safe = count
        if count == 0:
            break
        rain += 1
    print(max_safe)


if __name__ == '__main__':
    main()
