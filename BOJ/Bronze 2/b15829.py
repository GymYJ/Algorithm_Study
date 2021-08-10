import sys

L = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
answer = 0
for i, s in enumerate(string):
    answer = (answer + (ord(s) - 96) * (31 ** i)) % 1234567891
print(answer)
