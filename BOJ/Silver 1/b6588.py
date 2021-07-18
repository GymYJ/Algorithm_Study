import sys

check = [False, False] + [True for _ in range(999999)]
prime = []
for i in range(2, 1000001):
    if check[i]:
        prime.append(i)
        for j in range(i * 2, 1000001, i):
            check[j] = False
size = len(prime) - 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    a = prime[0]
    b = prime[-1]
    i = 0
    j = size
    low = 0
    high = size
    while low <= high:
        mid = (low + high) // 2
        if prime[mid] <= n:
            b = prime[mid]
            j = mid
            low = mid + 1
        else:
            high = mid - 1
    is_p = False
    while a != b:
        if a + b < n:
            i += 1
            a = prime[i]
        elif a + b > n:
            j -= 1
            b = prime[j]
        else:
            is_p = True
            break
    if a + b == n:
        is_p = True
    if is_p:
        print(n, '=', a, '+', b)
    else:
        print("Goldbach's conjecture is wrong.")
