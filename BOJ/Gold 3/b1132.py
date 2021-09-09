import sys

n = int(sys.stdin.readline())
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
dic = {}
count = {i: [0] * 13 for i in alphabet}
no_zero = set()
arr = []
for _ in range(n):
    temp = list(sys.stdin.readline().strip())
    arr.append(temp)
    no_zero.add(temp[0])
    rev = reversed(temp)
    for i, s in enumerate(rev):
        count[s][12 - i] += 1
        if count[s][12 - i] == 10:
            j = 1
            while count[s][12 - i - j + 1] == 10:
                count[s][12 - i - j] += 1
                count[s][12 - i - j + 1] = 0
                j += 1
total = []
for key in count:
    total.append(count[key] + [key])
total.sort(reverse=True)
num = 9
for i in range(10):
    temp = total[i][:13]
    if sum(temp) == 0:
        break
    dic[total[i][13]] = num
    num -= 1
tu = []
for key in dic:
    tu.append([dic[key], key])
tu.sort()
for i in range(len(tu) - 1):
    if tu[i][0] == 0 and tu[i][1] in no_zero:
        temp = tu[i][0]
        tu[i][0] = tu[i + 1][0]
        tu[i + 1][0] = temp
    else:
        break
for i in range(len(tu)):
    dic[tu[i][1]] = tu[i][0]
answer = 0
for string in arr:
    temp = ''
    for s in string:
        temp += str(dic[s])
    answer += int(temp)
print(answer)
