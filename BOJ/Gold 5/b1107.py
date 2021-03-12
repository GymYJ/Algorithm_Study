def main():
    n = input()
    m = int(input())
    broken = []
    if m != 0:
        broken = list(input().split())
    now = n
    if len(broken) == 10:
        print(abs(100 - int(n)))
        return
    do = False
    for b in broken:
        if b in now:
            do = True
            break
    index = 1
    while do:
        if int(n) - index >= 0:
            now = str(int(n) - index)
            do = False
            for b in broken:
                if b in now:
                    do = True
                    break
        if do:
            now = str(int(n) + index)
            do = False
            for b in broken:
                if b in now:
                    do = True
                    break
        index += 1
    if len(now) + abs(int(now) - int(n)) > abs(100 - int(n)):
        print(abs(100 - int(n)))
    else:
        print(len(now) + abs(int(now) - int(n)))


if __name__ == '__main__':
    main()
