import sys


def main():
    n = int(sys.stdin.readline())
    a, b, c, d, e, f = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(a + b + c + d + e + f - max(a, b, c, d, e, f))
        return
    min_one = min(a, b, c, d, e, f)
    min_two = min(a + b, a + c, a + d, a + e, b + c, b + d,
                  c + e, d + e, f + b, f + c, f + d, f + e)
    min_three = min(a + b + c, a + b + d, a + c + e, a + d + e,
                    f + b + c, f + b + d, f + c + e, f + d + e)
    answer = 0
    answer += min_three * 4
    answer += min_two * (n - 1) * 4 + min_two * (n - 2) * 4
    answer += min_one * (n - 1) * (n - 2) * 4 + min_one * (n - 2) * (n - 2)
    print(answer)


if __name__ == '__main__':
    main()
