import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
dic = {i: 0 for i in range(2, 21)}
for _ in range(k + 1):
    l = len(sys.stdin.readline().strip())
    arr.append(l)
    dic[l] += 1
answer = dic[arr[0]] - 1
left, right = 0, k + 1
while left < n - 1:
    dic[arr[left]] -= 1
    left += 1
    if right < n:
        l = len(sys.stdin.readline().strip())
        arr.append(l)
        dic[l] += 1
        right += 1
    answer += dic[arr[left]] - 1
print(answer)
