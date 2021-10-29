import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    m = int(sys.stdin.readline())
    arr = []
    for _ in range(m // 10 + 1):
        arr += list(map(int, sys.stdin.readline().split()))
    posi = []
    nega = []
    answer = []
    for i, num in enumerate(arr, start=1):
        if i % 2 == 1:
            if len(posi) == 0:
                posi.append(num)
            else:
                if -nega[0] <= num:
                    heapq.heappush(posi, num)
                else:
                    temp = heapq.heappop(nega)
                    heapq.heappush(posi, -temp)
                    heapq.heappush(nega, -num)
            answer.append(posi[0])
        else:
            if len(nega) == 0:
                if posi[0] >= num:
                    nega.append(-num)
                else:
                    temp = heapq.heappop(posi)
                    nega.append(-temp)
                    posi.append(num)
            else:
                if posi[0] <= num:
                    temp = heapq.heappop(posi)
                    heapq.heappush(nega, -temp)
                    heapq.heappush(posi, num)
                else:
                    heapq.heappush(nega, -num)
    print(len(answer))
    for i in range(0, len(answer) + 1, 10):
        print(*answer[i:i + 10])
