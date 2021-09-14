import sys
import heapq

n = int(sys.stdin.readline())
low_h = [-int(sys.stdin.readline())]
high_h = []
l_size, h_size = 1, 0
print(-low_h[0])
for i in range(1, n):
    num = int(sys.stdin.readline())
    if i % 2 == 1:
        if -low_h[0] > num:
            heapq.heappush(low_h, -num)
            if l_size > h_size:
                heapq.heappush(high_h, -heapq.heappop(low_h))
                h_size += 1
            else:
                l_size += 1
        else:
            heapq.heappush(high_h, num)
            if l_size < h_size:
                heapq.heappush(low_h, -heapq.heappop(high_h))
                l_size += 1
            else:
                h_size += 1
    else:
        if -low_h[0] > num:
            heapq.heappush(low_h, -num)
            l_size += 1
        else:
            heapq.heappush(high_h, num)
            h_size += 1
    if l_size >= h_size:
        print(-low_h[0])
    else:
        print(high_h[0])
