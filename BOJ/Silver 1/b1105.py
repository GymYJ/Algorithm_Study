import sys

l, r = sys.stdin.readline().split()

if len(l) != len(r):
    print(0)
else:
    answer = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                answer += 1
        else:
            break
    print(answer)
