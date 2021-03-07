import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    know = set()
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(temp[0]):
        know.add(temp[i + 1])
    party = []
    for _ in range(m):
        party.append(list(map(int, sys.stdin.readline().split()[1:])))
    visit = [0 for _ in range(m)]
    answer = m
    while True:
        truth = False
        for i in range(m):
            if visit[i] == 0:
                check = False
                for person in party[i]:
                    if person in know:
                        check = True
                        break
                if check:
                    visit[i] = 1
                    truth = True
                    answer -= 1
                    for person in party[i]:
                        know.add(person)
        if not truth:
            break
    print(answer)


if __name__ == '__main__':
    main()
