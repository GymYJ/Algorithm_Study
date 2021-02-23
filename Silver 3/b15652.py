import sys


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    answer = []

    def dfs(count, arr, index):
        nonlocal m
        nonlocal answer
        if count == m:
            answer.append(list(map(str, arr)))
            return
        for i in range(index, n + 1):
            dfs(count + 1, arr + [i], i)

    dfs(0, [], 1)
    for a in answer:
        print(' '.join(a))


if __name__ == '__main__':
    main()
