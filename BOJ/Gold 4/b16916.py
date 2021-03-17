import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

s_len = len(s)
p_len = len(p)

KMPtable = [0 for _ in range(len(p))]

j = 0
for i in range(1, p_len):
    while j > 0 and p[i] != p[j]:
        j = KMPtable[j - 1]
    if p[i] == p[j]:
        j += 1
        KMPtable[i] = j

j = 0
answer = 0
for i in range(s_len):
    while j > 0 and s[i] != p[j]:
        j = KMPtable[j - 1]
    if s[i] == p[j]:
        if j == p_len - 1:
            answer = 1
        else:
            j += 1

print(answer)
