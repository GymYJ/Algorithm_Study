while True:
    string = input()
    if string == '.':
        break
    stack = []
    size = 0
    is_p = True
    for s in string:
        if s == '(':
            stack.append(s)
            size += 1
        elif s == '[':
            stack.append(s)
            size += 1
        elif s == ')':
            if size == 0:
                is_p = False
                break
            if stack[-1] == '(':
                stack.pop()
                size -= 1
            else:
                is_p = False
                break
        elif s == ']':
            if size == 0:
                is_p = False
                break
            if stack[-1] == '[':
                stack.pop()
                size -= 1
            else:
                is_p = False
                break
    print('yes' if is_p and not stack else 'no')
