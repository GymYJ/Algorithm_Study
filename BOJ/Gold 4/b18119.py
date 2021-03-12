import sys

# python으로 안되서 c++로 함
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    word = set(sys.stdin.readline().strip())
    temp = ['0' for _ in range(26)]
    for w in word:
        temp[ord(w) - 97] = '1'
    arr.append(int(''.join(temp), 2))
forgot = ['1' for _ in range(26)]
for _ in range(m):
    o, x = sys.stdin.readline().split()
    if o == '1':
        forgot[ord(x) - 97] = '0'
    else:
        forgot[ord(x) - 97] = '1'
    forgot_bit = int(''.join(forgot), 2)
    answer = n
    for a in arr:
        if bin(a & forgot_bit) != a:
            answer -= 1
    print(answer)
