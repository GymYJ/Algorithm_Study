import copy


def main():
    n, m = list(map(int, input().split()))
    fri = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b = list(map(int, input().split()))
        fri[a].append(b)
        fri[b].append(a)
    day = -1
    answer = []
    end = False
    while not end:
        day += 1
        end = True
        count = 0
        cp_fri = copy.deepcopy(fri)
        for i in cp_fri:
            for j in cp_fri[i]:
                for k in cp_fri[j]:
                    if k not in fri[i] and k != i:
                        fri[i].append(k)
                        fri[k].append(i)
                        end = False
                        count += 1
        if count:
            answer.append(count)
    print(day)
    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
