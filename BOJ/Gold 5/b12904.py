import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())
s_len, t_len = len(s), len(t)
is_p = False
while True:
    if s_len == t_len:
        if s == t:
            is_p = True
        break
    back = t.pop()
    t_len -= 1
    if back == 'B':
        t.reverse()
print(1 if is_p else 0)
