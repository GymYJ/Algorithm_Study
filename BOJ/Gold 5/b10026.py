from collections import deque


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    visit = []
    visit2 = []
    x_list = [1, -1, 0, 0]
    y_list = [0, 0, -1, 1]
    count = 0
    count2 = 0
    for i in range(n):
        for j in range(n):
            if (i, j) not in visit:
                q = deque([(i, j)])
                visit.append((i, j))
                while q:
                    now = q.popleft()
                    color = arr[now[0]][now[1]]
                    for x, y in zip(x_list, y_list):
                        if 0 <= now[0] + x < n and 0 <= now[1] + y < n:
                            if arr[now[0] + x][now[1] + y] == color and (now[0] + x, now[1] + y) not in visit:
                                q.append((now[0] + x, now[1] + y))
                                visit.append((now[0] + x, now[1] + y))
                count += 1
            if (i, j) not in visit2:
                q = deque([(i, j)])
                visit2.append((i, j))
                while q:
                    now = q.popleft()
                    color = arr[now[0]][now[1]]
                    for x, y in zip(x_list, y_list):
                        if 0 <= now[0] + x < n and 0 <= now[1] + y < n:
                            if color == 'B':
                                if arr[now[0] + x][now[1] + y] == color and (now[0] + x, now[1] + y) not in visit2:
                                    q.append((now[0] + x, now[1] + y))
                                    visit2.append((now[0] + x, now[1] + y))
                            else:
                                if arr[now[0] + x][now[1] + y] in ['R', 'G'] and (now[0] + x, now[1] + y) not in visit2:
                                    q.append((now[0] + x, now[1] + y))
                                    visit2.append((now[0] + x, now[1] + y))
                count2 += 1
    print(count, count2)


if __name__ == '__main__':
    main()
