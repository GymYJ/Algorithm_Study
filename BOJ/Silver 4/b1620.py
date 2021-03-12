from collections import defaultdict

n, m = input().split()
n, m = int(n), int(m)
po = defaultdict(dict)
po_list = []
for i in range(n):
    temp = input()
    po[temp[0]][temp] = i + 1
    po_list.append(temp)
answer = []
for _ in range(m):
    temp = input()
    if 48 <= ord(temp[0]) <= 57:
        answer.append(po_list[int(temp) - 1])
    else:
        answer.append(po[temp[0]][temp])
for i in answer:
    print(i)
