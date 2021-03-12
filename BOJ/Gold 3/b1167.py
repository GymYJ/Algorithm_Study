import sys

# "트리의 지름을 구하는 공식은
# 임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고,
# 이 노드 B에서 가장 거리가 먼 노드 C를 구하게 되었을 때,
# B와 C 사이의 거리가 트리의 지름이 된다."
v = int(sys.stdin.readline())
dic = {i: {} for i in range(1, v + 1)}
for _ in range(v):
    temp = list(map(int, sys.stdin.readline().split()))
    node = temp[0]
    for i in range(1, len(temp) - 2, 2):
        dic[node][temp[i]] = temp[i + 1]
        dic[temp[i]][node] = temp[i + 1]


def dfs(now, length, before, res):
    for k in dic[now]:
        if res[k] == 0 and k != before:
            res[k] = length + dic[now][k]
            dfs(k, length + dic[now][k], now, res)


result = [0 for _ in range(v + 1)]
dfs(1, 0, 1, result)
start_node = result.index(max(result))
result2 = [0 for _ in range(v + 1)]
dfs(start_node, 0, start_node, result2)
print(max(result2))
