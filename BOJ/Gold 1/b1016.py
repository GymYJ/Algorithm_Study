import sys
from math import sqrt, ceil

low, high = map(int, sys.stdin.readline().split())
n = int(sqrt(high))
answer = [1 for _ in range(low, high + 1)]
arr = [i ** 2 for i in range(2, n + 1)]
for num in arr:
    index = ceil(low / num) * num - low
    while index <= high - low:
        answer[index] = 0
        index += num
print(sum(answer))
