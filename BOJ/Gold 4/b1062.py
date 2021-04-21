import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().split())
word = []
char = set()
for _ in range(n):
    temp = 0b0
    for s in sys.stdin.readline().strip():
        temp = temp | (1 << 26 - (ord(s) - 97))
        char.add(s)
    word.append(temp)
char = char.difference('a', 'c', 'i', 'n', 't')
if k < 5:
    print(0)
elif len(char) <= k - 5:
    print(n)
else:
    answer = 0
    remember = 0b101000001000010000010000000
    for ch in combinations(char, k - 5):
        for c in ch:
            remember = remember | (1 << 26 - (ord(c) - 97))
        count = 0
        for w in word:
            if remember | w == remember:
                count += 1
        answer = max(answer, count)
        remember = 0b101000001000010000010000000
    print(answer)
