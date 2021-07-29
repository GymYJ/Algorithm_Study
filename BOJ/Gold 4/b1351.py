import sys

sys.setrecursionlimit(1000000)


def recursion(num):
    global a, p, q
    if num == 0:
        return 1
    if a.get(num):
        return a[num]
    else:
        a[num] = recursion(num // q) + recursion(num // p)
        return a[num]


n, p, q = map(int, sys.stdin.readline().split())
a = {0: 1}
recursion(n)
print(a[n])
