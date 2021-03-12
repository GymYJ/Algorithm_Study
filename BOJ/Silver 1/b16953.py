import sys
from collections import deque


def main():
    a, b = list(map(int, sys.stdin.readline().split()))
    q = deque([(a, 1)])
    answer = -1
    while q:
        num, count = q.popleft()
        if num == b:
            answer = count
            break
        for i in [num * 2, num * 10 + 1]:
            if i <= b:
                q.append((i, count + 1))
    print(answer)


if __name__ == '__main__':
    main()
