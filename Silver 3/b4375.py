def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        num = 0
        count = 0
        while True:
            num = num * 10 + 1
            count += 1
            if num % n == 0:
                print(count)
                break


if __name__ == '__main__':
    main()
