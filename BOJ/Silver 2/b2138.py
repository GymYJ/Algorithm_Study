import sys


def change_zero(light):
    global target
    count = 1
    light[0] = 1 - light[0]
    light[1] = 1 - light[1]
    for i in range(1, len(light)):
        if light[i - 1] == target[i - 1]:
            continue
        else:
            count += 1
            light[i - 1] = 1 - light[i - 1]
            light[i] = 1 - light[i]
            if i < len(light) - 1:
                light[i + 1] = 1 - light[i + 1]
    if light == target:
        return count
    return 1000000


def no_change_zero(light):
    global target
    count = 0
    for i in range(1, len(light)):
        if light[i - 1] == target[i - 1]:
            continue
        else:
            count += 1
            light[i - 1] = 1 - light[i - 1]
            light[i] = 1 - light[i]
            if i < len(light) - 1:
                light[i + 1] = 1 - light[i + 1]
    if light == target:
        return count
    return 1000000


n = int(sys.stdin.readline())
now = list(map(int, list(sys.stdin.readline().strip())))
target = list(map(int, list(sys.stdin.readline().strip())))
answer = min(change_zero(now[:]), no_change_zero(now[:]))
if answer == 1000000:
    print(-1)
else:
    print(answer)
