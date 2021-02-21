def main():
    n = int(input())
    tree = []
    for _ in range(n):
        tree.append(list(map(int, list(str(input())))))
    answer = ''

    def cut(t, size):
        nonlocal answer
        init = t[0][0]
        for i in t:
            for j in i:
                if j != init:
                    resize = size // 2
                    answer += '('
                    cut([k[:resize] for k in t[:resize]], resize)
                    cut([k[resize:] for k in t[:resize]], resize)
                    cut([k[:resize] for k in t[resize:]], resize)
                    cut([k[resize:] for k in t[resize:]], resize)
                    answer += ')'
                    return
        answer += str(init)

    cut(tree, n)
    answer += ''
    print(answer)


if __name__ == '__main__':
    main()
