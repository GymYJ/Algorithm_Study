import sys

sys.setrecursionlimit(15000)


def dfs(bat, i, j, m, n):
    bat[i][j] = 0
    if j + 1 < m and bat[i][j + 1] == 1:
        bat = dfs(bat, i, j + 1, m, n)
    if j - 1 >= 0 and bat[i][j - 1] == 1:
        bat = dfs(bat, i, j - 1, m, n)
    if i + 1 < n and bat[i + 1][j] == 1:
        bat = dfs(bat, i + 1, j, m, n)
    if i - 1 >= 0 and bat[i - 1][j] == 1:
        bat = dfs(bat, i - 1, j, m, n)
    return bat


def main():
    a = int(input())
    answer = []
    for _ in range(a):
        m, n, k = input().split()
        bat = [[0 for _ in range(int(m))] for _ in range(int(n))]
        for _ in range(int(k)):
            x, y = input().split()
            bat[int(y)][int(x)] = 1
        count = 0
        for i in range(int(n)):
            for j in range(int(m)):
                if bat[i][j] == 1:
                    bat = dfs(bat, i, j, int(m), int(n))
                    count += 1
        answer.append(count)
    for i in answer:
        print(i)


if __name__ == '__main__':
    main()
