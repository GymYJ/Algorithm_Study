def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    target = list(map(int, input().split()))
    arr.sort()
    answer = []
    for i in target:
        left = 0
        right = n - 1
        find = False
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == i:
                find = True
                break
            elif arr[mid] > i:
                right = mid - 1
            else:
                left = mid + 1
        if find:
            answer.append(1)
        else:
            answer.append(0)
    print(' '.join(list(map(str, answer))))


if __name__ == '__main__':
    main()
