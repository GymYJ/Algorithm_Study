import sys


def f(n):
    count = 0

    k = 0
    while 2 ** k <= n:
        pattern = 2 ** (k + 1)
        p_count = (n + 1) // pattern

        # (완성된 패턴의 갯수) * (패턴의 길이의 절반 = 한 패턴에서 1은 절반이 나오기 때문)
        # ex) n = 12, k = 2 -> 패턴의 크기는 8이므로 패턴은 0 ~ 7까지 한번 반복
        count += p_count * (pattern // 2)

        # ex 계속) 나머지인 8 ~ 12에서 이진수 셋째자리의 1의 개수는 12에서 1
        left = (n + 1) % pattern
        count += max(0, left - pattern // 2)
        k += 1

    return count


a, b = map(int, sys.stdin.readline().split())
print(f(b) - f(a - 1))
