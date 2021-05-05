import sys

sys.setrecursionlimit(1000000)


def dfs(cur):
    global check, tree, dp
    check[cur] = 1  # 방문체크
    dp[cur][0] = 0  # 본인이 얼리가 아닐 때
    dp[cur][1] = 1  # 본인이 얼리일 때
    for i in tree[cur]:  # 연결된 노드 탐색
        if check[i] == 0:
            dfs(i)
            dp[cur][0] += dp[i][1]  # 본인이 얼리가 아니면 친구는 무조건 얼리여야 함
            dp[cur][1] += min(dp[i][0], dp[i][1])  # 본인이 얼리면 친구는 얼리든 아니든 상관없음


n = int(sys.stdin.readline())
tree = {i: [] for i in range(1, n + 1)}
check = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [[0, 0] for _ in range(n + 1)]

dfs(1)
print(min(dp[1][0], dp[1][1]))
