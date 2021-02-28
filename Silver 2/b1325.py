import sys
import copy
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    dic = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        dic[b].append(a)
    dp = [0 for _ in range(n + 1)]
    visit = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        cp_visit = copy.deepcopy(visit)
        q = deque([i])
        cp_visit[i] = 1
        count = 0
        while q:
            now = q.popleft()
            count += 1
            for j in dic[now]:
                if cp_visit[j] == 0:
                    cp_visit[j] = 1
                    q.append(j)
        dp[i] = count
    value = max(dp)
    answer = []
    for i in range(1, n + 1):
        if dp[i] == value:
            answer.append(str(i))
    print(' '.join(answer))


if __name__ == '__main__':
    main()
