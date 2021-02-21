def main():
    n = int(input())
    t_list = list(map(int, input().split()))
    t_list.sort()
    answer = 0
    total = 0
    for i in range(n):
        total += t_list[i]
        answer += total
    print(answer)


if __name__ == '__main__':
    main()