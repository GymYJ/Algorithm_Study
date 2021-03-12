def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    answer = 0
    for i in range(n):
        w = arr[i] * (n - i)
        if answer < w:
            answer = w
    print(answer)


if __name__ == '__main__':
    main()
