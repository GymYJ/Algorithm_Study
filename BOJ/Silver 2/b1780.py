def main():
    n = int(input())
    paper = []
    for _ in range(n):
        row = list(map(int, input().split()))
        paper.append(row)

    minus = 0
    zero = 0
    one = 0

    def cut(p, size):
        nonlocal minus
        nonlocal zero
        nonlocal one
        init = p[0][0]
        for i in p:
            for j in i:
                if j != init:
                    resize = size // 3
                    cut([k[:resize] for k in p[:resize]], resize)
                    cut([k[:resize] for k in p[resize:2 * resize]], resize)
                    cut([k[:resize] for k in p[2 * resize:]], resize)
                    cut([k[resize: 2 * resize] for k in p[:resize]], resize)
                    cut([k[resize: 2 * resize] for k in p[resize:2 * resize]], resize)
                    cut([k[resize: 2 * resize] for k in p[2 * resize:]], resize)
                    cut([k[2 * resize:] for k in p[:resize]], resize)
                    cut([k[2 * resize:] for k in p[resize:2 * resize]], resize)
                    cut([k[2 * resize:] for k in p[2 * resize:]], resize)
                    return
        if init == -1:
            minus += 1
        elif init == 0:
            zero += 1
        else:
            one += 1

    cut(paper, n)
    print(minus)
    print(zero)
    print(one)


if __name__ == '__main__':
    main()
