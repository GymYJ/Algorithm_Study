import sys

d, n = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
pizza = list(map(int, sys.stdin.readline().split()))
new_oven = [oven[0]]
mini = oven[0]
for i in range(1, d):
    mini = min(mini, oven[i])
    new_oven.append(mini)
answer = 0
left = 0
right = d - 1
check = True
for i in range(len(pizza)):
    if i != 0 and pizza[i] <= pizza[i - 1]:
        answer = right + 1
        right -= 1
    else:
        if right < 0 or pizza[i] > new_oven[0]:
            answer = 0
            break
        index = 0
        while left <= right:
            mid = (left + right) // 2
            if new_oven[mid] < pizza[i]:
                right = mid - 1
            else:
                index = mid
                left = mid + 1
        answer = index + 1
        right = index - 1
        left = 0
print(answer)
