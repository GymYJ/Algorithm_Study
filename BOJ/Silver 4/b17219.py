def main():
    n, m = list(map(int, input().split()))
    dic = {}
    for _ in range(n):
        address, password = input().split()
        dic[address] = password
    for _ in range(m):
        print(dic[input()])


if __name__ == '__main__':
    main()
