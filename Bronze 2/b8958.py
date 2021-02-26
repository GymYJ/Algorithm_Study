t = int(input())
for _ in range(t):
    result = input()
    score = 0
    now = 0
    for s in result:
        if s == 'O':
            now += 1
            score += now
        else:
            now = 0
    print(score)
