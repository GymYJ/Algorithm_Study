import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
see = [0 for _ in range(n)]
for i in range(n):
    high, low = -1, sys.maxsize
    for j in range(i - 1, -1, -1):
        if arr[j] >= arr[i]:
            if high < (arr[j] - arr[i]) / (i - j):
                high = (arr[j] - arr[i]) / (i - j)
                see[i] += 1
        else:
            if high == -1:
                if low > (arr[i] - arr[j]) / (i - j):
                    low = (arr[i] - arr[j]) / (i - j)
                    see[i] += 1
    high, low = -1, sys.maxsize
    for j in range(i + 1, n):
        if arr[j] >= arr[i]:
            if high < (arr[j] - arr[i]) / (j - i):
                high = (arr[j] - arr[i]) / (j - i)
                see[i] += 1
        else:
            if high == -1:
                if low > (arr[i] - arr[j]) / (j - i):
                    low = (arr[i] - arr[j]) / (j - i)
                    see[i] += 1
print(max(see))
