from collections import Counter

a = input().upper()
counter = Counter(a)
answer = ''
max_use = max(counter.values())
for c in counter:
    if counter[c] == max_use:
        if answer == '':
            answer = c
        else:
            answer = '?'
            break
print(answer)
