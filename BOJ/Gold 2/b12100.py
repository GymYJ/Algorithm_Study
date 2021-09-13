import sys


def dfs(board, count):
    global n, answer
    max_value = 0
    for i in range(n):
        for j in range(n):
            max_value = max(max_value, board[i][j])
    answer = max(answer, max_value)
    if count == 5:
        return
    for k in range(4):
        new_board = [[0 for _ in range(n)] for _ in range(n)]
        if k == 0:
            for j in range(n):
                lst = [board[i][j] for i in range(n)]
                idx = 0
                target = 1
                while idx < n - 1 and target <= n - 1:
                    if lst[idx] != 0:
                        if lst[target] == 0:
                            target += 1
                        elif lst[idx] == lst[target]:
                            lst[idx] *= 2
                            lst[target] = 0
                            idx = target + 1
                            target = idx + 1
                        else:
                            idx = target
                            target += 1
                    else:
                        idx += 1
                        target = idx + 1
                idx = 0
                for num in lst:
                    if num != 0:
                        new_board[idx][j] = num
                        idx += 1
        elif k == 1:
            for j in range(n):
                lst = [board[i][j] for i in range(n)]
                idx = n - 1
                target = n - 2
                while idx > 0 and target >= 0:
                    if lst[idx] != 0:
                        if lst[target] == 0:
                            target -= 1
                        elif lst[idx] == lst[target]:
                            lst[idx] *= 2
                            lst[target] = 0
                            idx = target - 1
                            target = idx - 1
                        else:
                            idx = target
                            target -= 1
                    else:
                        idx -= 1
                        target = idx - 1
                idx = n - 1
                lst.reverse()
                for num in lst:
                    if num != 0:
                        new_board[idx][j] = num
                        idx -= 1
        elif k == 2:
            for i in range(n):
                lst = [board[i][j] for j in range(n)]
                idx = 0
                target = 1
                while idx < n - 1 and target <= n - 1:
                    if lst[idx] != 0:
                        if lst[target] == 0:
                            target += 1
                        elif lst[idx] == lst[target]:
                            lst[idx] *= 2
                            lst[target] = 0
                            idx = target + 1
                            target = idx + 1
                        else:
                            idx = target
                            target += 1
                    else:
                        idx += 1
                        target = idx + 1
                idx = 0
                for num in lst:
                    if num != 0:
                        new_board[i][idx] = num
                        idx += 1
        else:
            for i in range(n):
                lst = [board[i][j] for j in range(n)]
                idx = n - 1
                target = n - 2
                while idx > 0 and target >= 0:
                    if lst[idx] != 0:
                        if lst[target] == 0:
                            target -= 1
                        elif lst[idx] == lst[target]:
                            lst[idx] *= 2
                            lst[target] = 0
                            idx = target - 1
                            target = idx - 1
                        else:
                            idx = target
                            target -= 1
                    else:
                        idx -= 1
                        target = idx - 1
                idx = n - 1
                lst.reverse()
                for num in lst:
                    if num != 0:
                        new_board[i][idx] = num
                        idx -= 1
        dfs(new_board, count + 1)


n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
answer = 0
dfs(arr, 0)
print(answer)
