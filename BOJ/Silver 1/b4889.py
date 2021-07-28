import sys

number = 1
while True:
    s = sys.stdin.readline().strip()
    if s[0] == '-':
        break
    answer = 0
    stack = []
    size = 0
    for i in s:
        if i == '}':
            if size == 0:
                stack.append('{')
                size += 1
                answer += 1
            else:
                stack.pop()
                size -= 1
        else:
            stack.append('{')
            size += 1
    if size > 0:
        answer += size // 2
    print(f'{number}.', answer)
    number += 1
