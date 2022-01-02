def find_prime_number():
    global prime
    check = [True for _ in range(150)]
    for i in range(2, 150):
        if check[i]:
            prime.append(i)
            for j in range(i, 150, i):
                check[j] = False


n = int(input())
prime = []
find_prime_number()
for i in range(len(prime) - 1):
    if prime[i] * prime[i + 1] > n:
        print(prime[i] * prime[i + 1])
        break