from collections import defaultdict


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dic = defaultdict(list)
        for _ in range(n):
            name, kinds = input().split()
            dic[kinds].append(name)
        answer = 1
        for k in dic:
            answer *= len(dic[k]) + 1
        print(answer - 1)


if __name__ == '__main__':
    main()
