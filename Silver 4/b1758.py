import sys


def main():
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.sort(reverse=True)
    answer = 0
    for i, t in enumerate(arr):
        if t - i <= 0:
            continue
        else:
            answer += t - i
    print(answer)


if __name__ == '__main__':
    main()
