import sys

n, l = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
answer = 0
for i in range(n):
    now = 0
    road = [0 for _ in range(n)]
    check = True
    for j in range(n):
        if now == 0:
            now = arr[i][j]
            continue
        if now == arr[i][j]:
            continue
        elif now + 1 == arr[i][j]:
            for k in range(1, l + 1):
                if j - k >= 0 and arr[i][j - k] == arr[i][j] - 1 and road[j - k] == 0:
                    road[j - k] = 1
                else:
                    check = False
                    break
            if not check:
                break
            now = arr[i][j]
        elif now - 1 == arr[i][j]:
            for k in range(l):
                if j + k < n and arr[i][j + k] == now - 1 and road[j + k] == 0:
                    road[j + k] = 1
                else:
                    check = False
                    break
            if not check:
                break
            now = arr[i][j]
        else:
            check = False
            break
    if check:
        answer += 1

for j in range(n):
    now = 0
    road = [0 for _ in range(n)]
    check = True
    for i in range(n):
        if now == 0:
            now = arr[i][j]
            continue
        if now == arr[i][j]:
            continue
        elif now + 1 == arr[i][j]:
            for k in range(1, l + 1):
                if i - k >= 0 and arr[i - k][j] == arr[i][j] - 1 and road[i - k] == 0:
                    road[i - k] = 1
                else:
                    check = False
                    break
            if not check:
                break
            now = arr[i][j]
        elif now - 1 == arr[i][j]:
            for k in range(l):
                if i + k < n and arr[i + k][j] == now - 1 and road[i + k] == 0:
                    road[i + k] = 1
                else:
                    check = False
                    break
            if not check:
                break
            now = arr[i][j]
        else:
            check = False
            break
    if check:
        answer += 1
print(answer)
