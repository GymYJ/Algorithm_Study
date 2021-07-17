import sys

s, e, q = sys.stdin.readline().split()
s = int(''.join(s.split(":")))
e = int(''.join(e.split(":")))
q = int(''.join(q.split(":")))
member = {}
answer = 0
while True:
    try:
        time, name = sys.stdin.readline().split()
    except ValueError:
        break
    time = int(''.join(time.split(":")))
    if time <= s:
        member[name] = 1
    elif e <= time <= q:
        if member.get(name) == 1:
            answer += 1
            member[name] += 1
print(answer)
