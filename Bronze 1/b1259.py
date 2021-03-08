import sys

while True:
    num = sys.stdin.readline().strip()
    if num == '0':
        break
    yes = True
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            yes = False
    if yes:
        print('yes')
    else:
        print('no')
