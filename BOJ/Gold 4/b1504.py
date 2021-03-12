import sys
import heapq
from math import inf


def main():
    n, e = map(int, sys.stdin.readline().split())
    arr = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    for a in range(1, n + 1):
        arr[a][a] = 0
    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        if arr[a][b] > c:
            arr[a][b] = c
            arr[b][a] = c
    v1, v2 = map(int, sys.stdin.readline().split())

    def dijkstra(start):
        nonlocal n
        nonlocal arr
        dist = [inf for _ in range(n + 1)]
        dist[start] = 0
        queue = []
        heapq.heappush(queue, [dist[start], start])

        while queue:
            now_dist, now = heapq.heappop(queue)

            if now_dist > dist[now]:
                continue

            for next_node, next_dist in enumerate(arr[now]):
                distance = now_dist + next_dist
                if dist[next_node] > distance:
                    dist[next_node] = distance
                    heapq.heappush(queue, [distance, next_node])

        return dist

    dist_1 = dijkstra(1)
    dist_v1 = dijkstra(v1)
    dist_v2 = dijkstra(v2)
    answer = min(dist_1[v1] + dist_v1[v2] + dist_v2[n], dist_1[v2] + dist_v2[v1] + dist_v1[n])
    print(answer if answer != inf else -1)


if __name__ == '__main__':
    main()
