def main():
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        for i in range(1, 9):
            if arr[i - 1] != i:
                print('mixed')
                return
        print('ascending')
    elif arr[0] == 8:
        for i in range(8):
            if arr[i] != 8 - i:
                print('mixed')
                return
        print('descending')
    else:
        print('mixed')


if __name__ == '__main__':
    main()
