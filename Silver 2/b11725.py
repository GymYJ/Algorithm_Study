import sys
from collections import deque


def main():
    n = int(sys.stdin.readline())
    dic = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        a, b = list(map(int, sys.stdin.readline().split()))
        dic[a].append(b)
        dic[b].append(a)
    q = deque([1])
    visit = [0 for _ in range(n + 1)]
    visit[1] = 1
    while q:
        now = q.popleft()
        for i in dic[now]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = now
    for i in range(2, n + 1):
        print(visit[i])


if __name__ == '__main__':
    main()
