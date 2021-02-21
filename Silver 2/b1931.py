from collections import deque

n = int(input())
c_list = []
for _ in range(n):
    s, e = input().split()
    c_list.append((int(e), int(s)))
c_list.sort()
c_list = deque(c_list)
now = c_list.popleft()[0]
count = 1
while c_list:
    temp = c_list.popleft()
    if temp[1] >= now:
        now = temp[0]
        count += 1
print(count)
