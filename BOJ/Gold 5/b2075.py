import sys
import heapq

n = int(sys.stdin.readline())
heap = []
size = 0
for _ in range(n):
    for i in list(map(int, sys.stdin.readline().split())):
        if size < n:
            heapq.heappush(heap, i)
            size += 1
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
print(heap[0])
