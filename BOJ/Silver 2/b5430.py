from collections import deque


def main():
    t = int(input())
    answer = []
    for _ in range(t):
        p = input()
        n = int(input())
        arr = deque(input().lstrip('[').rstrip(']').split(','))
        if n == 0:
            arr = []
        stop = False
        reverse = False
        for s in p:
            if s == 'R':
                if reverse:
                    reverse = False
                else:
                    reverse = True
            else:
                if len(arr) == 0:
                    answer.append('error')
                    stop = True
                    break
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
        if not stop:
            if reverse:
                arr.reverse()
            answer.append('[' + ','.join(arr) + ']')
    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
