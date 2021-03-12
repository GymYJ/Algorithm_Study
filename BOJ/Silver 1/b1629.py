import sys


def main():
    a, b, c = list(map(int, sys.stdin.readline().split()))

    def solution(aa, bb):
        nonlocal c
        if bb == 1:
            return aa % c
        else:
            value = solution(aa, bb // 2)
            if bb % 2 == 0:
                return value * value % c
            else:
                return value * value * aa % c

    print(solution(a, b))


if __name__ == '__main__':
    main()
