import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
heapq.heapify(arr)
first = []
second = []
answer = 0
while arr:
    now = heapq.heappop(arr)
    if now < 10:
        continue
    elif now == 10:
        answer += 1
    elif now % 10 == 0:
        heapq.heappush(first, now)
    else:
        heapq.heappush(second, now)
count = 0
while count < m and (first or second):
    if first:
        now = heapq.heappop(first)
        count += 1
        answer += 1
        if now - 10 == 10:
            answer += 1
        else:
            heapq.heappush(first, now - 10)
    else:
        now = heapq.heappop(second)
        count += 1
        answer += 1
        if now - 10 >= 10:
            heapq.heappush(second, now - 10)
print(answer)
