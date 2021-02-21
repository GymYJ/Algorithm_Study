def main():
    n = int(input())
    pn = 'I'
    for _ in range(n):
        pn += 'O'
        pn += 'I'
    m = int(input())
    s = input()
    now = s[:n * 2 + 1]
    answer = 0
    i = 1
    before = False
    if pn == now:
        before = True
        answer += 1
    while i < m:
        if before:
            if i + 1 < m and s[i] == 'O' and s[i + 1] == 'I':
                answer += 1
                i += 2
                continue
            else:
                before = False
        else:
            if i + n * 2 + 1 >= m:
                break
            now = s[i:i + n * 2 + 1]
            if pn == now:
                answer += 1
                i += n * 2 + 1
                before = True
                continue
            else:
                i += 1

    print(answer)


if __name__ == '__main__':
    main()
