import sys


def do_op(op):
    global stack, size
    if op[0] == 'NUM':
        stack.append(int(op[1]))
        size += 1
    elif op[0] == 'POP':
        if size == 0:
            return False
        stack.pop()
        size -= 1
    elif op[0] == 'INV':
        if size == 0:
            return False
        num = stack.pop()
        stack.append(-num)
    elif op[0] == 'DUP':
        if size == 0:
            return False
        stack.append(stack[-1])
        size += 1
    elif op[0] == 'SWP':
        if size <= 1:
            return False
        a = stack.pop()
        b = stack.pop()
        stack.append(a)
        stack.append(b)
    elif op[0] == 'ADD':
        if size <= 1:
            return False
        a = stack.pop()
        b = stack.pop()
        if abs(b + a) > 10 ** 9:
            return False
        stack.append(b + a)
        size -= 1
    elif op[0] == 'SUB':
        if size <= 1:
            return False
        a = stack.pop()
        b = stack.pop()
        if abs(b - a) > 10 ** 9:
            return False
        stack.append(b - a)
        size -= 1
    elif op[0] == 'MUL':
        if size <= 1:
            return False
        a = stack.pop()
        b = stack.pop()
        if abs(b * a) > 10 ** 9:
            return False
        stack.append(b * a)
        size -= 1
    elif op[0] == 'DIV':
        if size <= 1:
            return False
        a = stack.pop()
        b = stack.pop()
        if a == 0:
            return False
        temp = abs(b) // abs(a)
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            stack.append(-temp)
        else:
            stack.append(temp)
        size -= 1
    elif op[0] == 'MOD':
        if size <= 1:
            return False
        a = stack.pop()
        b = stack.pop()
        if a == 0:
            return False
        temp = abs(b) % abs(a)
        if b < 0:
            stack.append(-temp)
        else:
            stack.append(temp)
        size -= 1
    return True


while True:
    ops = []
    while True:
        temp = sys.stdin.readline().split()
        if temp[0] == 'END':
            break
        elif temp[0] == 'QUIT':
            sys.exit()
        ops.append(temp)
    n = int(sys.stdin.readline())
    for _ in range(n):
        stack = [int(sys.stdin.readline())]
        size = 1
        error = False
        for op in ops:
            if not do_op(op):
                error = True
                break
        if error:
            print('ERROR')
        else:
            print(stack[-1] if size == 1 else 'ERROR')
    print()
    sys.stdin.readline()
