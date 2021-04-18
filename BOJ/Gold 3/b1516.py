# 내가 한 풀이(성공)
# import sys
#
# n = int(sys.stdin.readline())
# parent = {i: [] for i in range(1, n + 1)}
# answer = [0 for _ in range(n + 1)]
# build = [False for _ in range(n + 1)]
# build[0] = True
# build_time = [0]
# for i in range(1, n + 1):
#     temp = list(map(int, sys.stdin.readline().split()))
#     time = temp[0]
#     build_time.append(time)
#     prnt = temp[1:]
#     if prnt[0] == -1:
#         answer[i] = time
#         build[i] = True
#         continue
#     parent[i] = prnt[:-1]
#
# while not all(build):
#     for i in range(1, n + 1):
#         if not build[i]:
#             if all([build[j] for j in parent[i]]):
#                 answer[i] = max([answer[j] for j in parent[i]]) + build_time[i]
#                 build[i] = True
# for i in range(1, n + 1):
#     print(answer[i])

# 위상정렬을 사용한 정석적인 풀이
from collections import defaultdict, deque

N = int(input())
answer = [0] * (N + 1)
cost = [0] * (N + 1)
degree = [0] * (N + 1)
Q = deque()

graph = defaultdict(list)
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    cost[i] = temp[0]

    for element in temp[1:-1]:
        graph[element].append(i)
        degree[i] += 1

for i in range(1, N + 1):
    if degree[i] == 0:
        Q.append(i)
        answer[i] = cost[i]

while Q:
    now = Q.popleft()
    for element in graph[now]:
        degree[element] -= 1
        answer[element] = max(answer[element], cost[element] + answer[now])

        if degree[element] == 0:
            Q.append(element)

for i in range(1, len(answer)):
    print(answer[i])
