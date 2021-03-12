n, x = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
for num in arr:
    if num < x:
        answer.append(num)
print(' '.join(map(str, answer)))
