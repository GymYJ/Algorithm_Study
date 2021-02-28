import sys
from collections import deque


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dic = {i: [] for i in range(-1, n)}
    for i, num in enumerate(arr):
        dic[num].append(i)
    del_node = int(sys.stdin.readline())
    q = deque([-1])
    count = 0
    while q:
        now = q.popleft()
        if len(dic[now]) == 0:
            count += 1
            continue
        temp = 0
        for i in dic[now]:
            if i != del_node:
                q.append(i)
                temp += 1
        if temp == 0 and now != -1:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
