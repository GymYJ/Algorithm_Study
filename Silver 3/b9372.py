import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = list(map(int, sys.stdin.readline().split()))
        dic = {i: [] for i in range(1, n + 1)}
        for _ in range(m):
            a, b = list(map(int, sys.stdin.readline().split()))
            dic[a].append(b)
            dic[b].append(a)
        print(n - 1)


if __name__ == '__main__':
    main()
