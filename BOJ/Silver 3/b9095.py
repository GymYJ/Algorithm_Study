def main():
    count = 0

    def dfs(num, target):
        nonlocal count
        if num == target:
            count += 1
            return
        for i in range(1, 4):
            if num + i <= target:
                dfs(num + i, target)

    t = int(input())
    answer = []
    for _ in range(t):
        dfs(0, int(input()))
        answer.append(count)
        count = 0

    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
