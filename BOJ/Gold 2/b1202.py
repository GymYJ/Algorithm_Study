import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
je = []
for _ in range(n):
    heapq.heappush(je, list(map(int, sys.stdin.readline().split())))
bag = []
for _ in range(k):
    bag.append(int(sys.stdin.readline()))
bag.sort()
answer = 0
temp = []
for b in bag:
    while je and b >= je[0][0]:
        heapq.heappush(temp, -je[0][1])
        heapq.heappop(je)
    if temp:
        answer += (-1) * heapq.heappop(temp)
    elif not je:
        break
print(answer)
