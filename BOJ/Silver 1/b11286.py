from collections import defaultdict
import heapq


def main():
    n = int(input())
    q = []
    dic = defaultdict(int)
    answer = []
    for _ in range(n):
        num = int(input())
        if num == 0:
            if len(q) == 0:
                answer.append(0)
            else:
                number = heapq.heappop(q)
                if dic[number] > 0:
                    answer.append(-1 * number)
                    dic[number] -= 1
                else:
                    answer.append(number)
        else:
            if num < 0:
                dic[abs(num)] += 1
            elif num not in dic:
                dic[num] = 0
            heapq.heappush(q, abs(num))
    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
