def main():
    n, k = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    answer = 0
    while k > 0:
        for coin in sorted(arr, reverse=True):
            if k // coin > 0:
                temp = k // coin
                answer += temp
                k -= temp * coin
                break
    print(answer)


if __name__ == '__main__':
    main()
