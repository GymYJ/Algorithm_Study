import re

n = int(input())
q = re.compile("^[A-F]?A+F+C+[A-F]?$")
for _ in range(n):
    sent = input()
    if q.match(sent):
        print('Infected!')
    else:
        print('Good')
