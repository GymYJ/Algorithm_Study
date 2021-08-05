import sys


def dfs(now_arr, energy, size):
    global arr, answer
    if size == 2:
        if answer < energy:
            answer = energy
        return
    for i in range(1, size - 1):
        dfs(now_arr[:i] + now_arr[i + 1:], energy + now_arr[i - 1] * now_arr[i + 1], size - 1)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
dfs(arr, 0, n)
print(answer)
