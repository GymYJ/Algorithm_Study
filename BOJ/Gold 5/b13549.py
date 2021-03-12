import sys
from collections import deque


def main():
    n, k = map(int, sys.stdin.readline().split())
    q = deque([[0, n]])
    visit = [-1 for _ in range(100001)]
    visit[n] = 0
    time = 0
    find = False
    while q:
        t, now = q.popleft()
        if now == k:
            if find:
                if time > t:
                    time = t
            else:
                find = True
                time = t
        else:
            if find:
                if time > t + 1:
                    for x in [now - 1, now + 1]:
                        if 0 <= x <= 100000 and (visit[x] == -1 or visit[x] > t + 1):
                            q.append([t + 1, x])
                            visit[x] = t + 1
                if time > t:
                    if 0 <= now * 2 <= 100000 and (visit[now * 2] == -1 or visit[now * 2] > t):
                        q.append([t, now * 2])
                        visit[now * 2] = t
            else:
                for x in [now - 1, now + 1]:
                    if 0 <= x <= 100000 and (visit[x] == -1 or visit[x] > t + 1):
                        q.append([t + 1, x])
                        visit[x] = t + 1
                if 0 <= now * 2 <= 100000 and (visit[now * 2] == -1 or visit[now * 2] > t):
                    q.append([t, now * 2])
                    visit[now * 2] = t
    print(time)


if __name__ == '__main__':
    main()
