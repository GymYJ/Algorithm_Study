from collections import defaultdict

dud = defaultdict(list)
n, m = input().split()
for _ in range(int(n)):
    temp = input()
    dud[temp[0]].append(temp)
for i in dud:
    dud[i].sort()
answer = []
count = 0
for _ in range(int(m)):
    temp = input()
    left = 0
    right = len(dud[temp[0]]) - 1
    while left <= right:
        mid = (left + right) // 2
        if dud[temp[0]][mid] == temp:
            answer.append(temp)
            count += 1
            break
        elif dud[temp[0]][mid] < temp:
            left = mid + 1
        else:
            right = mid - 1
answer.sort()
print(count)
for a in answer:
    print(a)
