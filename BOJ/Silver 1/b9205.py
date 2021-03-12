from collections import deque


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        now = list(map(int, input().split()))
        conve = []
        q = deque([])
        for _ in range(n):
            c = tuple(map(int, input().split()))
            conve.append(c)
            if abs(now[0] - c[0]) + abs(now[1] - c[1]) <= 1000:
                q.append(c)
        desti = tuple(map(int, input().split()))
        if abs(now[0] - desti[0]) + abs(now[1] - desti[1]) <= 1000:
            print('happy')
            continue
        visit = []
        happy = False
        while q:
            now = q.popleft()
            visit.append(now)
            if abs(now[0] - desti[0]) + abs(now[1] - desti[1]) <= 1000:
                happy = True
                break
            for c in conve:
                if abs(now[0] - c[0]) + abs(now[1] - c[1]) <= 1000 and c not in visit and c not in q:
                    q.append(c)
        if happy:
            print('happy')
        else:
            print('sad')


if __name__ == '__main__':
    main()
