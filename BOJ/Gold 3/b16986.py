import sys


def check(a, b):
    global arr
    if arr[a][b] == 2:
        return [1, 0]
    else:
        return [0, 1]


def dfs(ji, ky, mi, j_w, k_w, m_w, k_idx, m_idx):
    global n, k, arr, kyung, minho, use
    if j_w == k:
        print(1)
        sys.exit()
    if k_w == k or m_w == k:
        return
    if sum(use) == n:
        return
    if ji and ky:
        if k_idx >= 20:
            return
        for i in range(1, n + 1):
            if use[i] == 0:
                use[i] = 1
                a, b = check(i, kyung[k_idx])
                if a == 1:
                    dfs(True, False, True, j_w + 1, k_w, m_w, k_idx + 1, m_idx)
                else:
                    dfs(False, True, True, j_w, k_w + 1, m_w, k_idx + 1, m_idx)
                use[i] = 0
    elif ji and mi:
        if m_idx >= 20:
            return
        for i in range(1, n + 1):
            if use[i] == 0:
                use[i] = 1
                a, b = check(i, minho[m_idx])
                if a == 1:
                    dfs(True, True, False, j_w + 1, k_w, m_w, k_idx, m_idx + 1)
                else:
                    dfs(False, True, True, j_w, k_w, m_w + 1, k_idx, m_idx + 1)
                use[i] = 0
    else:
        if k_idx >= 20 or m_idx >= 20:
            return
        a, b = check(kyung[k_idx], minho[m_idx])
        if a == 1:
            dfs(True, True, False, j_w, k_w + 1, m_w, k_idx + 1, m_idx + 1)
        else:
            dfs(True, False, True, j_w, k_w, m_w + 1, k_idx + 1, m_idx + 1)
    return


n, k = map(int, sys.stdin.readline().split())
arr = [[-1 for _ in range(n + 1)]]
for _ in range(n):
    arr.append([-1] + list(map(int, sys.stdin.readline().split())))
kyung = list(map(int, sys.stdin.readline().split()))
minho = list(map(int, sys.stdin.readline().split()))
use = [0 for _ in range(n + 1)]
dfs(True, True, False, 0, 0, 0, 0, 0)
print(0)
