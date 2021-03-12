import sys
import heapq


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(arr)
    for _ in range(m):
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        c = a + b
        heapq.heappush(arr, c)
        heapq.heappush(arr, c)
    print(sum(arr))


if __name__ == '__main__':
    main()
