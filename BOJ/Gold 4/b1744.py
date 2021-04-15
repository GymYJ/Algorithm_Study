import sys
import heapq

n = int(sys.stdin.readline())
negative = []
n_size = 0
one = 0
positive = []
p_size = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    if num < 1:
        negative.append(num)
        n_size += 1
    elif num == 1:
        one += 1
    else:
        positive.append(-num)
        p_size += 1
heapq.heapify(negative)
heapq.heapify(positive)
answer = one
while n_size > 1:
    answer += (heapq.heappop(negative) * heapq.heappop(negative))
    n_size -= 2
if n_size == 1:
    answer += negative[0]

while p_size > 1:
    answer += (heapq.heappop(positive) * heapq.heappop(positive))
    p_size -= 2
if p_size == 1:
    answer += -positive[0]
print(answer)
