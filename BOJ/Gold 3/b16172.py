import sys

is_pass = {str(i): True for i in range(10)}
S = ''
for i in sys.stdin.readline().strip():
    if is_pass.get(i):
        continue
    S += i
K = sys.stdin.readline().strip()
s_len = len(S)
k_len = len(K)
kmp_table = [0 for _ in range(k_len)]

j = 0
for i in range(1, k_len):
    while j > 0 and K[i] != K[j]:
        j = kmp_table[j - 1]
    if K[i] == K[j]:
        j += 1
        kmp_table[i] = j

j = 0
for i in range(s_len):
    while j > 0 and S[i] != K[j]:
        j = kmp_table[j - 1]
    if S[i] == K[j]:
        if j == k_len - 1:
            print(1)
            sys.exit()
        else:
            j += 1
print(0)
