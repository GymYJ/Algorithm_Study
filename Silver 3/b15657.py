import sys


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    answer = []

    def dfs(count, array, index):
        nonlocal m
        nonlocal arr
        nonlocal answer
        if count == m:
            answer.append(list(map(str, array)))
            return
        for i in range(index, n):
            dfs(count + 1, array + [arr[i]], i)

    dfs(0, [], 0)
    for a in answer:
        print(' '.join(a))


if __name__ == '__main__':
    main()
