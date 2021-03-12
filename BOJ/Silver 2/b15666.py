import sys


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    answer = set()

    def bt(count, now, index):
        nonlocal n
        nonlocal m
        nonlocal arr
        nonlocal answer
        if count == m:
            if now not in answer:
                print(' '.join(list(map(str, now))))
                answer.add(now)
            return
        for i in range(index, n):
            bt(count + 1, now + tuple([arr[i]]), i)

    bt(0, (), 0)


if __name__ == '__main__':
    main()
