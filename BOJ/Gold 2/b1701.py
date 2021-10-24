import sys


def make_kmp(s):
    kmp = [0 for _ in range(len(s))]
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = kmp[j - 1]
        if s[i] == s[j]:
            j += 1
            kmp[i] = j
    return max(kmp)


string = sys.stdin.readline().strip()
answer = 0
for i in range(len(string)):
    answer = max(answer, make_kmp(string[i:len(string)]))
print(answer)
