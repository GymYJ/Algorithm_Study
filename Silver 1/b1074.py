def main():
    n, r, c = input().split()
    n, r, c = int(n), int(r), int(c)
    answer = 0
    for i in range(n, 0, -1):
        if r < 2**(i - 1) and c < 2**(i - 1):
            continue
        elif r < 2**(i - 1) <= c:
            answer += 2**(i - 1) * 2**(i - 1)
            c -= 2**(i - 1)
        elif r >= 2**(i - 1) > c:
            answer += 2**(i - 1) * 2**(i - 1) * 2
            r -= 2**(i - 1)
        else:
            answer += 2**(i - 1) * 2**(i - 1) * 3
            r -= 2**(i - 1)
            c -= 2**(i - 1)
    print(answer)


if __name__ == '__main__':
    main()
