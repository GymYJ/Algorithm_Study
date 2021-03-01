import string

s = input()
alphabet = list(string.ascii_lowercase)
answer = [-1 for _ in range(26)]
for i, a in enumerate(alphabet):
    if a in s:
        answer[i] = s.index(a)
print(' '.join(map(str, answer)))
