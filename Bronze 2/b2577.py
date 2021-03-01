a = int(input())
b = int(input())
c = int(input())
num = str(a * b * c)
dic = {i: 0 for i in range(10)}
for s in num:
    dic[int(s)] += 1
for n in dic.values():
    print(n)
