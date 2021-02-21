from collections import defaultdict
from math import inf


def main():
    t = int(input())
    answer = []
    for _ in range(t):
        k = int(input())
        dic = defaultdict(int)
        maxi = -inf
        mini = inf
        for _ in range(k):
            op, num = input().split()
            if op == 'I':
                dic[int(num)] += 1
                if int(num) > maxi:
                    maxi = int(num)
                if int(num) < mini:
                    mini = int(num)
            else:
                if len(dic) == 0:
                    continue
                elif num == '1':
                    if dic[maxi] == 1:
                        dic.pop(maxi)
                    else:
                        dic[maxi] -= 1
                    if len(dic) == 0:
                        maxi = -inf
                        mini = inf
                    else:
                        maxi = max(dic)
                else:
                    if dic[mini] == 1:
                        dic.pop(mini)
                    else:
                        dic[mini] -= 1
                    if len(dic) == 0:
                        maxi = -inf
                        mini = inf
                    else:
                        mini = min(dic)
        if len(dic) == 0:
            answer.append('EMPTY')
        else:
            answer.append((maxi, mini))
    for a in answer:
        if a == 'EMPTY':
            print(a)
        else:
            print(a[0], a[1])


if __name__ == '__main__':
    main()
