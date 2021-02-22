def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    count = 0
    arr.reverse()
    before = arr[0]
    for i in range(1, n):
        now = arr[i]
        while now >= before:
            now -= 1
            count += 1
        before = now
    print(count)


if __name__ == '__main__':
    main()
