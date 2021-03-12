import sys


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    inf = sys.maxsize
    arr = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        arr[i][i] = 0
    for _ in range(m):
        s, e, c = map(int, sys.stdin.readline().split())
        if arr[s][e] > c:
            arr[s][e] = c

    def floyd():
        nonlocal n
        nonlocal arr
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if arr[i][j] > arr[i][k] + arr[k][j]:
                        arr[i][j] = arr[i][k] + arr[k][j]

    floyd()
    for a in arr[1:]:
        print(' '.join(list(map(lambda x: '0' if x == inf else str(x), a[1:]))))


if __name__ == '__main__':
    main()
