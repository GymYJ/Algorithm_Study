def main():
    int(input())
    x = list(map(int, input().split()))
    sort_x = sorted(list(set(x)))
    dic = {}
    for i, xi in enumerate(sort_x):
        dic[xi] = i
    answer = [str(dic[i]) for i in x]
    print(' '.join(answer))


if __name__ == '__main__':
    main()
