def main():
    n, m = list(map(int, input().split()))
    trees = list(map(int, input().split()))
    trees.sort()
    left = 0
    right = trees[-1]
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in trees:
            if i > mid:
                total += i - mid
        if total >= m:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)


if __name__ == '__main__':
    main()
