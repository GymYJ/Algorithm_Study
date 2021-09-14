import sys
from collections import deque


def main():
    inf = sys.maxsize
    tc = int(sys.stdin.readline())
    for _ in range(tc):
        n, m, w = map(int, sys.stdin.readline().split())
        dic = {i: [] for i in range(1, n + 1)}
        start_point = []
        for _ in range(m):
            s, e, t = map(int, sys.stdin.readline().split())
            dic[s].append((e, t))
            dic[e].append((s, t))
        for _ in range(w):
            s, e, t = map(int, sys.stdin.readline().split())
            dic[s].append((e, -t))
            start_point.append(e)
        can = False
        for i in start_point:
            visit_time = [inf for _ in range(n + 1)]
            visit_time[i] = 0
            q = deque(dic[i])
            while q:
                now, now_time = q.popleft()
                if now == i:
                    if now_time < 0:
                        can = True
                        break
                    else:
                        continue
                for next_point, use_time in dic[now]:
                    if visit_time[next_point] > now_time + use_time:
                        visit_time[next_point] = now_time + use_time
                        q.append((next_point, now_time + use_time))
            if can:
                break
        print('YES' if can else 'NO')


if __name__ == '__main__':
    main()
