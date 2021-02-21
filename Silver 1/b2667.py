from collections import deque


def main():
    n = int(input())
    jido = []
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        jido.append(list(map(int, list(input()))))
    group = []
    for i in range(n):
        for j in range(n):
            if jido[i][j] == 0:
                continue
            else:
                if visit[i][j] == 1:
                    continue
                else:
                    visit[i][j] = 1
                    q = deque([(i, j)])
                    count = 0
                    while q:
                        x, y = q.popleft()
                        count += 1
                        if x < n - 1 and visit[x + 1][y] == 0 and jido[x + 1][y] == 1:
                            visit[x + 1][y] = 1
                            q.append((x + 1, y))
                        if y < n - 1 and visit[x][y + 1] == 0 and jido[x][y + 1] == 1:
                            visit[x][y + 1] = 1
                            q.append((x, y + 1))
                        if x > 0 and visit[x - 1][y] == 0 and jido[x - 1][y] == 1:
                            visit[x - 1][y] = 1
                            q.append((x - 1, y))
                        if y > 0 and visit[x][y - 1] == 0 and jido[x][y - 1] == 1:
                            visit[x][y - 1] = 1
                            q.append((x, y - 1))
                    group.append(count)
    print(len(group))
    for i in sorted(group):
        print(i)


if __name__ == '__main__':
    main()
