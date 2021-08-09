import sys
from collections import Counter

n = int(sys.stdin.readline())
counter = Counter(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = []
for i in arr:
    answer.append(counter[i])
print(*answer)
