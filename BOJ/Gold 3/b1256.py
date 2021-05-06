import sys


def dfs(idx, nn, mm):
    global answer, k
    if k == idx:
        for _ in range(nn):
            answer += 'a'
        for _ in range(mm):
            answer += 'z'
        print(answer)
        sys.exit()
    mp = 1
    for i in range(1, mm + 1):
        mp *= i
    mp_d = mp // mm
    np_d = 1
    i = 1
    while nn > 0:
        np_d = np_d * i
        idx += mp // (mp_d * np_d)
        if idx >= k:
            for _ in range(nn - 1):
                answer += 'a'
            answer += 'z'
            idx -= mp // (mp_d * np_d)
            dfs(idx + 1, i, mm - 1)
        mp = mp * (mm + i)
        nn -= 1
        i += 1
    print(-1)


n, m, k = map(int, sys.stdin.readline().split())
answer = ''
dfs(1, n, m)
