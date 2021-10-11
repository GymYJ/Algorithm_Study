import sys

yut = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
       [10, 13, 16, 19], [30, 28, 27, 26], [20, 22, 24, 25, 30, 35, 40]]
position = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [5, 21, 22, 23], [15, 24, 25, 26], [10, 27, 28, 29, 30, 31, 20]]
pi_po = [[0, 0] for _ in range(5)]


def dfs(depth, score):
    global result, pi_po, s
    if depth == 10:
        result = max(result, score)
        return
    for i in range(1, 5):
        x, y = pi_po[i]
        if x == -1:
            continue
        else:
            ny = y + s[depth]
            if x == 0:
                if 20 < ny:
                    pi_po[i] = [-1, -1]
                elif ny == 5:
                    pi_po[i] = [1, 0]
                elif ny == 10:
                    pi_po[i] = [3, 0]
                elif ny == 15:
                    pi_po[i] = [2, 0]
                else:
                    pi_po[i] = [x, ny]
            elif x == 1:
                if ny >= 8:
                    pi_po[i] = [-1, -1]
                elif ny >= 4:
                    pi_po[i] = [3, ny - 1]
                else:
                    pi_po[i] = [x, ny]
            elif x == 2:
                if ny >= 8:
                    pi_po[i] = [-1, -1]
                elif ny >= 4:
                    pi_po[i] = [3, ny - 1]
                else:
                    pi_po[i] = [x, ny]
            elif x == 3:
                if ny > 6:
                    pi_po[i] = [-1, -1]
                else:
                    pi_po[i] = [x, ny]
            nx, ny = pi_po[i]
            if nx != -1:
                is_p = True
                for j in range(1, 5):
                    if i == j:
                        continue
                    a, b = pi_po[j]
                    if a == -1:
                        continue
                    if position[a][b] == position[nx][ny]:
                        is_p = False
                if is_p:
                    dfs(depth + 1, score + yut[nx][ny])
            else:
                dfs(depth + 1, score)
            pi_po[i] = [x, y]


s = list(map(int, sys.stdin.readline().split()))
result = 0
dfs(0, 0)
print(result)
