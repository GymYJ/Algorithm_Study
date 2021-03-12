from collections import deque
from math import inf


def main():
    n, m = list(map(int, input().split()))
    miro = []
    for _ in range(n):
        miro.append(list(map(int, list(input()))))
    visit = [[inf for _ in range(m)] for _ in range(n)]

    mini = 10001

    q = deque([(0, 0, 1)])
    while q:
        x, y, length = q.popleft()
        if x == n - 1 and y == m - 1:
            if mini > length:
                mini = length
                continue
        if x < n - 1:
            if visit[x + 1][y] > length + 1 and miro[x + 1][y] == 1:
                q.append((x + 1, y, length + 1))
                visit[x + 1][y] = length + 1
        if y < m - 1:
            if visit[x][y + 1] > length + 1 and miro[x][y + 1] == 1:
                q.append((x, y + 1, length + 1))
                visit[x][y + 1] = length + 1
        if x > 0:
            if visit[x - 1][y] > length + 1 and miro[x - 1][y] == 1:
                q.append((x - 1, y, length + 1))
                visit[x - 1][y] = length + 1
        if y > 0:
            if visit[x][y - 1] > length + 1 and miro[x][y - 1] == 1:
                q.append((x, y - 1, length + 1))
                visit[x][y - 1] = length + 1

    print(mini)


if __name__ == '__main__':
    main()
