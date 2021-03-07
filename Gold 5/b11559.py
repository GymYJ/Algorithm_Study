import sys
from collections import deque


def main():
    arr = []
    for _ in range(12):
        arr.append(list(sys.stdin.readline()))
    field = []
    for i in range(6):
        temp = []
        for j in range(11, -1, -1):
            temp.append(arr[j][i])
        field.append(temp)
    answer = 0
    x_list = [-1, 1, 0, 0]
    y_list = [0, 0, -1, 1]
    while True:
        boom = False
        crush = []
        visit = [[0 for _ in range(12)] for _ in range(6)]
        for i in range(6):
            for j in range(12):
                if field[i][j] != '.':
                    now = field[i][j]
                    q = deque([(i, j)])
                    temp = [(i, j)]
                    visit[i][j] = 1
                    while q:
                        now_x, now_y = q.popleft()
                        for x, y in zip(x_list, y_list):
                            next_x = now_x + x
                            next_y = now_y + y
                            if 0 <= next_x < 6 and 0 <= next_y < 12 and visit[next_x][next_y] == 0 \
                                    and field[next_x][next_y] == now:
                                visit[next_x][next_y] = 1
                                q.append((next_x, next_y))
                                temp.append((next_x, next_y))
                    if len(temp) >= 4:
                        crush += temp
                        boom = True
        if boom:
            answer += 1
            crush.sort(reverse=True)
            for i, j in crush:
                del field[i][j]
                field[i].append('.')
        else:
            break
    print(answer)


if __name__ == '__main__':
    main()
