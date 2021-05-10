import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append((int(sys.stdin.readline()), i))

sorted_arr = sorted(arr)
answer = 1
for i in range(n):
    answer = max(answer, sorted_arr[i][1] - i + 1)
print(answer)
