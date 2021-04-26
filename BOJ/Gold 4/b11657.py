import sys
from math import inf

n, m = map(int, sys.stdin.readline().split())
distance = [inf for _ in range(n + 1)]  # 거리 값
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def bellman_ford(start):
    global distance, graph
    distance[start] = 0  # 시작 정점 거리는 0
    # 간선 개수(V-1)만큼 반복
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, wei in graph[node]:  # 각 정점마다 모든 인접 정점들을 탐색
                # (기존 인접 정점까지의 거리 > 기존 현재 정점까지 거리 + 현재 정점부터 인접 정점까지 거리)인 경우 갱신
                if distance[neighbor] > distance[node] + wei:
                    distance[neighbor] = distance[node] + wei

    # 음수 사이클 존재 여부 검사 : V-1번 반복 이후에도 갱신할 거리 값이 존재한다면 음수 사이클 존재
    for node in graph:
        for neighbor, wei in graph[node]:
            if distance[neighbor] > distance[node] + wei:
                return False

    return True


result = bellman_ford(1)
if result:
    for d in distance[2:]:
        print(d if d != inf else -1)
else:
    print(-1)
