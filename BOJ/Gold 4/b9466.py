import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    answer = n
    group = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if group[i] == 0:
            group[i] = 1
            visit = [i]
            pick = arr[i]
            while True:
                if group[pick] == 1:
                    if pick in visit:
                        answer -= (len(visit) - visit.index(pick))
                    break
                else:
                    group[pick] = 1
                    visit.append(pick)
                    pick = arr[pick]
    print(answer)
