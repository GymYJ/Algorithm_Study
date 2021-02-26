import sys

sys.setrecursionlimit(100000)


def main():
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        return

    dic = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        p, s, w = map(int, sys.stdin.readline().split())
        dic[p].append((s, w))
        dic[s].append((p, w))

    def dfs(now, now_w, before, result):
        nonlocal dic
        for next_n, next_w in dic[now]:
            if result[next_n] == 0 and next_n != before:
                result[next_n] = now_w + next_w
                dfs(next_n, now_w + next_w, now, result)

    res = [0 for _ in range(n + 1)]
    dfs(1, 0, 1, res)
    start_node = res.index(max(res))
    res = [0 for _ in range(n + 1)]
    dfs(start_node, 0, start_node, res)
    print(max(res))


if __name__ == '__main__':
    main()
