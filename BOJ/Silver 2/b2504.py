import sys

string = sys.stdin.readline().strip()
stack = []
size = 0
answer = 0
for s in string:
    temp = []
    if s == '(' or s == '[':
        stack.append(s)
        size += 1
    elif s == ')':
        if size == 0:
            answer = 0
            break
        while type(stack[-1]) == int:
            temp.append(stack.pop())
        if stack[-1] != '(':
            answer = 0
            break
        stack.pop()
        size -= 1
        if len(temp) == 0:
            stack.append(2)
        else:
            stack.append(2 * sum(temp))
    elif s == ']':
        if size == 0:
            answer = 0
            break
        while type(stack[-1]) == int:
            temp.append(stack.pop())
        if stack[-1] != '[':
            answer = 0
            break
        stack.pop()
        size -= 1
        if len(temp) == 0:
            stack.append(3)
        else:
            stack.append(3 * sum(temp))
    if size == 0:
        answer += stack.pop()
if size != 0:
    answer = 0
print(answer)
