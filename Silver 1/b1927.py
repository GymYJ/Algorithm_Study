import heapq

hq = []
answer = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(hq) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)
for a in answer:
    print(a)