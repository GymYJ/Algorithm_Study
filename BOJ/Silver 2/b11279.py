import heapq


def main():
    n = int(input())
    h = []
    answer = []
    for _ in range(n):
        num = int(input())
        if num == 0:
            if len(h) == 0:
                answer.append(0)
            else:
                answer.append(heapq.heappop(h)[1])
        else:
            heapq.heappush(h, (-num, num))
    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
