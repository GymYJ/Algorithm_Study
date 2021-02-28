import sys
from collections import deque


def main():
    n = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    dic = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        dic[x].append(y)
        dic[y].append(x)
    q = deque([(a, 0)])
    visit = [0 for _ in range(n + 1)]
    visit[a] = 1
    relation = [0 for _ in range(n + 1)]
    while q:
        now, chon = q.popleft()
        relation[now] = chon
        if now == b:
            break
        for i in dic[now]:
            if visit[i] == 0:
                visit[i] = 1
                q.append((i, chon + 1))
    if visit[b] == 0:
        print(-1)
    else:
        print(relation[b])


if __name__ == '__main__':
    main()
