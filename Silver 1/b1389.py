from collections import deque
from math import inf


def main():
    n, m = list(map(int, input().split()))
    friend = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b = list(map(int, input().split()))
        friend[a].append(b)
        friend[b].append(a)

    mini = inf
    num = 0
    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        q = deque([(i, 0)])
        count = 0
        while q:
            now, kb = q.popleft()
            visit[now] = 1
            for f in friend[now]:
                if visit[f] == 0 and f not in [j[0] for j in q]:
                    q.append((f, kb + 1))
                    count += kb + 1
        if mini > count:
            mini = count
            num = i
    print(num)


if __name__ == '__main__':
    main()
