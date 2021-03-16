import sys
from itertools import permutations

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
operator = []
for i, o in enumerate(oper):
    operator += [i for _ in range(o)]
maxi = (-1) * sys.maxsize
mini = sys.maxsize
for i in permutations(operator, n - 1):
    num = arr[0]
    for j in range(n - 1):
        if i[j] == 0:
            num += arr[j + 1]
        elif i[j] == 1:
            num -= arr[j + 1]
        elif i[j] == 2:
            num *= arr[j + 1]
        else:
            if num < 0 and arr[j + 1] > 0:
                num = (num * -1) // arr[j + 1] * (-1)
            elif num > 0 and arr[j + 1] < 0:
                num = num // (-1 * arr[j + 1]) * (-1)
            else:
                num = num // arr[j + 1]
    if maxi < num:
        maxi = num
    if mini > num:
        mini = num
print(maxi)
print(mini)
