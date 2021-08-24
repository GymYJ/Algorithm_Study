import sys
import heapq

n = int(sys.stdin.readline())
oils = []
for _ in range(n):
    heapq.heappush(oils, list(map(int, sys.stdin.readline().split())))
L, P = map(int, sys.stdin.readline().split())

oil = P
move = []
answer = 0
while oil < L:
    while oils and oils[0][0] <= oil:
        loc, re = heapq.heappop(oils)
        heapq.heappush(move, [-re, loc])

    if not move:
        answer = -1
        break
    re, loc = heapq.heappop(move)
    oil += -re
    answer += 1
print(answer)
