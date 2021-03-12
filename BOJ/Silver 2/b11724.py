def main():
    n, m = list(map(int, input().split()))
    node = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = list(map(int, input().split()))
        node[u].append(v)
        node[v].append(u)
    visit = [0] * (n + 1)
    count = 0

    def dfs(now):
        nonlocal visit
        nonlocal node
        for i in node[now]:
            if visit[i] == 0:
                visit[i] = 1
                dfs(i)

    for i in range(1, n + 1):
        if visit[i] == 0:
            dfs(i)
            count += 1
    print(count)


if __name__ == '__main__':
    main()
