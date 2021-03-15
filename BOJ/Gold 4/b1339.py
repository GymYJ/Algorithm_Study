import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dic = defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().strip()
    k = len(word) - 1
    for w in word:
        dic[w] += pow(10, k)
        k -= 1
num = [i for i in dic.values()]
num.sort(reverse=True)
answer = 0
k = 9
for n in num:
    answer += n * k
    k -= 1
print(answer)
