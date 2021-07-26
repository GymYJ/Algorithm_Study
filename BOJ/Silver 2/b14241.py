import sys
import heapq

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
heapq.heapify(arr)
answer = 0
while n > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    answer += a * b
    heapq.heappush(arr, a + b)
    n -= 1
print(answer)
