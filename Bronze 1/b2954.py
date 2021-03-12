sent = input()
answer = ''
index = 0
while index < len(sent):
    if sent[index] in ['a', 'e', 'i', 'o', 'u']:
        answer += sent[index]
        index += 3
    else:
        answer += sent[index]
        index += 1
print(answer)
