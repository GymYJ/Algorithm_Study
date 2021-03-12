import sys

string = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()
boom_len = len(boom)
arr = []
stack = []
temp = []
index = 0
for s in string:
    if s != boom[index]:
        if len(temp) == 0:
            storage = []
            while stack:
                storage.append(stack.pop())
            while storage:
                for i in storage.pop():
                    arr.append(i)
            arr.append(s)
        else:
            index = 0
            stack.append(temp)
            if s != boom[index]:
                storage = []
                while stack:
                    storage.append(stack.pop())
                while storage:
                    for i in storage.pop():
                        arr.append(i)
                arr.append(s)
            temp = []
    if s == boom[index]:
        temp.append(s)
        index += 1
        if index == boom_len:
            if stack:
                temp = stack.pop()
                index = len(temp)
            else:
                temp = []
                index = 0
storage = []
while stack:
    storage.append(stack.pop())
while storage:
    for i in storage.pop():
        arr.append(i)
for i in temp:
    arr.append(i)
print(''.join(arr) if len(arr) != 0 else 'FRULA')
