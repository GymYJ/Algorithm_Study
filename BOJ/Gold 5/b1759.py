import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
mo = []
ja = []
for s in sys.stdin.readline().split():
    if s in ['a', 'e', 'i', 'o', 'u']:
        mo.append(s)
    else:
        ja.append(s)
mo.sort()
ja.sort()
answer = []
for i in range(1, l - 1):
    for m in combinations(mo, i):
        for j in combinations(ja, l - i):
            temp = list(m) + list(j)
            temp.sort()
            answer.append(temp)
answer.sort()
for a in answer:
    print(''.join(a))
