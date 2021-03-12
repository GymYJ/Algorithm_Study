from collections import deque


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    answer = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        visit = []
        q = deque([j for j in range(n) if arr[i][j] == 1])
        while q:
            now = q.popleft()
            answer[i][now] = 1
            visit.append(now)
            for j in range(n):
                if arr[now][j] == 1 and j not in visit:
                    q.append(j)
    for a in answer:
        print(' '.join(list(map(str, a))))


if __name__ == '__main__':
    main()
