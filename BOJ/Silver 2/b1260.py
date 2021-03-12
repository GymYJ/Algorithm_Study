from collections import deque


def main():
    n, m, v = list(map(int, input().split()))
    line = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b = list(map(int, input().split()))
        line[a].append(b)
        line[b].append(a)

    visit = [0] * (n + 1)
    dfs_seq = []

    def dfs(now):
        nonlocal line
        nonlocal visit
        nonlocal dfs_seq
        visit[now] = 1
        dfs_seq.append(str(now))
        for i in sorted(line[now]):
            if visit[i] == 0:
                dfs(i)

    dfs(v)

    visit = [0] * (n + 1)
    bfs_seq = []
    q = deque([v])
    while q:
        now = q.popleft()
        visit[now] = 1
        bfs_seq.append(str(now))
        for i in sorted(line[now]):
            if visit[i] == 0 and i not in q:
                q.append(i)

    print(' '.join(dfs_seq))
    print(' '.join(bfs_seq))


if __name__ == '__main__':
    main()
