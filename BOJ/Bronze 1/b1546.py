n = int(input())
arr = list(map(int, input().split()))
max_score = max(arr)
answer = 0
for a in arr:
    answer += (a / max_score) * 100
print(answer / n)
