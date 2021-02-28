import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        day = list(map(int, sys.stdin.readline().split()))
        day.reverse()
        answer = 0
        now_max = 0
        low_sum = 0
        count = 0
        for d in day:
            if now_max < d:
                answer += now_max * count - low_sum
                count = 0
                low_sum = 0
                now_max = d
            else:
                low_sum += d
                count += 1
        answer += now_max * count - low_sum
        print(answer)


if __name__ == '__main__':
    main()
