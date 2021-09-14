import sys

t = sys.stdin.readline().replace('\n', '')
p = sys.stdin.readline().replace('\n', '')
t_len = len(t)
p_len = len(p)

table = [0 for _ in range(len(p))]

j = 0
for i in range(1, p_len):
    while j > 0 and p[i] != p[j]:
        j = table[j - 1]
    if p[i] == p[j]:
        j += 1
        table[i] = j

j = 0
count = 0
answer = []
for i in range(t_len):
    while j > 0 and t[i] != p[j]:
        j = table[j - 1]
    if t[i] == p[j]:
        if j == p_len - 1:
            answer.append(i - p_len + 2)
            count += 1
            j = table[j]
        else:
            j += 1

print(count)
print(' '.join(list(map(str, answer))))
