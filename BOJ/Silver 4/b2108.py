import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
counter = Counter(arr)
most = []
maxi = 0
for key in counter:
    if counter[key] > maxi:
        maxi = counter[key]
        most = [key]
    elif counter[key] == maxi:
        most.append(key)
print(round(sum(arr) / n))
print(arr[n // 2])
if len(most) > 1:
    most.sort()
    print(most[1])
else:
    print(most[0])
print(arr[-1] - arr[0])
