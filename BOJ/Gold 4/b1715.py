import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))
answer = 0
while n > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    total = a + b
    answer += total
    heapq.heappush(heap, total)
    n -= 1
print(answer)
