import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort()
heap = []
answer = 0
left = 0
for s, e in arr:
    if left == 0:
        if len(heap) > 0 and heap[0] <= s:
            heapq.heappop(heap)
        else:
            answer += 1
    else:
        left -= 1
    heapq.heappush(heap, e)
print(answer)
