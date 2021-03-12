def main():
    n = int(input())
    if n == 0:
        num = ['1']
    else:
        num = n
        for i in range(n - 1, 0, -1):
            num = num*i
        num = list(str(num))
        num.reverse()
    count = 0
    for i in num:
        if i != '0':
            break
        count += 1
    print(count)


if __name__ == '__main__':
    main()
