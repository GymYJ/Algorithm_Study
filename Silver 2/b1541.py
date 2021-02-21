from collections import deque


def main():
    exp = input()
    num = ''
    cal = []
    for i in exp:
        if i == '+' or i == '-':
            cal.append(num)
            cal.append(i)
            num = ''
        else:
            num += i
    cal.append(num)
    cal = deque(cal)
    num = int(cal.popleft())
    keep = []
    while cal:
        op = cal.popleft()
        if op == '-':
            while cal:
                if cal[0] != '-' and cal[0] != '+':
                    keep.append(int(cal.popleft()))
                elif cal[0] == '+':
                    cal.popleft()
                else:
                    break
            num -= sum(keep)
            keep = []
        elif op == '+':
            num += int(cal.popleft())
    print(num)


if __name__ == '__main__':
    main()
