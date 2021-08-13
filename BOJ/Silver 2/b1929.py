import sys


def find_prime_number(mm, nn):
    global prime
    check = [True for _ in range(nn + 1)]
    for i in range(2, mm):
        if check[i]:
            for j in range(i, nn + 1, i):
                check[j] = False
    if mm == 1:
        mm = 2
    for i in range(mm, nn + 1):
        if check[i]:
            prime.append(i)
            for j in range(i, nn + 1, i):
                check[j] = False


m, n = map(int, sys.stdin.readline().split())
prime = []
find_prime_number(m, n)
for i in prime:
    print(i)
