import sys

n = int(sys.stdin.readline())
first = 666
while n != 0:
    if '666' in str(first):
        n -= 1
        if n == 0:
            break
    first = first + 1
print(first)
