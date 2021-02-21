from collections import deque


def main():
    t = int(input())
    answer = []
    for _ in range(t):
        a, b = list(map(int, input().split()))
        visit = [0 for _ in range(10000)]
        visit[a] = 1
        q = deque([(a, '')])
        while q:
            now, operation = q.popleft()
            if now == b:
                answer.append(operation)
                break
            d = now * 2 % 10000
            s = now - 1 if now > 0 else 9999
            d1 = now // 1000
            d2 = now // 100 - d1 * 10
            d3 = now // 10 - d2 * 10 - d1 * 100
            d4 = now - d3 * 10 - d2 * 100 - d1 * 1000
            l = d2 * 1000 + d3 * 100 + d4 * 10 + d1
            r = d4 * 1000 + d1 * 100 + d2 * 10 + d3
            for num, op in [(d, 'D'), (s, 'S'), (l, 'L'), (r, 'R')]:
                if visit[num] == 0:
                    q.append((num, operation + op))
                    visit[num] = 1
    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
