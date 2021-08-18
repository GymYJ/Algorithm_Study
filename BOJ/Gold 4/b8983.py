import sys

m, n, l = map(int, sys.stdin.readline().split())
marr = list(map(int, sys.stdin.readline().split()))
marr.sort()
animal = []
for _ in range(n):
    animal.append(list(map(int, sys.stdin.readline().split())))
count = 0
for a, b in animal:
    left = 0
    right = m - 1
    while left < right:
        mid = (left + right) // 2
        if marr[mid] < a:
            left = mid + 1
        else:
            right = mid
    if abs(marr[right] - a) + b <= l or abs(marr[right - 1] - a) + b <= l:
        count += 1
print(count)
