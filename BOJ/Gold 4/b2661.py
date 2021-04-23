import sys


def dfs(now):
    global n, answer
    if len(now) == n:
        answer = now
        return True
    for i in ['1', '2', '3']:
        check = True
        size = len(now) + 1
        size = size // 2
        while size >= 1:
            if size == 1:
                if now[-1] == i:
                    check = False
                    break
            else:
                if now[-(size * 2 - 1):-(size - 1)] == now[-(size - 1):] + i:
                    check = False
                    break
            size -= 1
        if check:
            if dfs(now + i):
                return True
    return False


n = int(sys.stdin.readline())
answer = ''
dfs('1')
print(answer)
