import sys
from collections import deque


def main():
    n, k = map(int, sys.stdin.readline().split())
    q = deque([(0, n)])
    time = 0
    count = 0
    find = False
    visit = [0 for _ in range(100001)]
    visit[n] = 1
    while q:
        t, now = q.popleft()
        if now == k:
            if find:
                if time == t:
                    count += 1
            else:
                find = True
                time = t
                count += 1
        else:
            if find:
                if t < time:
                    for x in [now - 1, now + 1, now * 2]:
                        if 0 <= x <= 100000 and (visit[x] == 0 or visit[x] >= t + 1):
                            q.append((t + 1, x))
                            visit[x] = t + 1
            else:
                for x in [now - 1, now + 1, now * 2]:
                    if 0 <= x <= 100000 and (visit[x] == 0 or visit[x] >= t + 1):
                        q.append((t + 1, x))
                        visit[x] = t + 1
    print(time)
    print(count)


if __name__ == '__main__':
    main()
