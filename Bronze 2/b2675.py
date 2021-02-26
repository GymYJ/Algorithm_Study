t = int(input())
for _ in range(t):
    r, s = input().split()
    temp = ''
    for i in s:
        for _ in range(int(r)):
            temp += i
    print(temp)