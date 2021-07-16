import sys
from collections import Counter

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(str, sys.stdin.readline().split())
    a = list(a)
    b = list(b)
    if Counter(a) != Counter(b):
        print(-1)
        continue
    answer = 0
    for i in range(1, len(a) - 1):
        if a[i] != b[i]:
            count = 0
            index = i
            while True:
                if a[index] == b[i]:
                    temp = a[i]
                    a[i] = a[index]
                    a[index] = temp
                    break
                else:
                    index += 1
                    count += 1
            answer += count
    print(answer)
