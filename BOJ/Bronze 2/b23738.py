import sys

dic = {'A': 'a', 'B': 'v', 'E': 'ye', 'K': 'k', 'M': 'm', 'H': 'n',
       'O': 'o', 'P': 'r', 'C': 's', 'T': 't', 'Y': 'u', 'X': 'h'}

s = sys.stdin.readline().strip()
answer = ''
for c in s:
    answer += dic[c]
print(answer)
