import sys

n = int(sys.stdin.readline())
arr = [i for i in range(1, n + 1)]
question = list(map(int, sys.stdin.readline().split()))
factorial = [1] * n
for i in range(2, n):
    factorial[i] = factorial[i - 1] * i
if question[0] == 1:
    num = question[1] - 1
    answer = []
    while arr:
        temp = num // factorial[-1]
        num = num % factorial[-1]
        factorial.pop()
        answer.append(arr[temp])
        arr.remove(arr[temp])
    print(' '.join(list(map(str, answer))))
else:
    question = question[1:]
    answer = 1
    for i, num in enumerate(question, start=1):
        if num == arr[0]:
            arr.remove(num)
        else:
            for j, a in enumerate(arr):
                if num == a:
                    answer += factorial[n - i] * j
                    break
            arr.remove(num)
    print(answer)
