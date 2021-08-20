import sys


def find_level(node):
    global k
    level = 0
    total = 1
    while True:
        if node <= total:
            break
        level += 1
        total += k ** level
    return level


def find_parent(node):
    global k
    if (node - 1) % k == 0:
        return node // k
    return (node - 1) // k + 1


n, k, q = map(int, sys.stdin.readline().split())
for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    if k == 1:
        print(abs(a - b))
        continue
    a_len, b_len = 0, 0
    a_lev, b_lev = find_level(a), find_level(b)
    if a_lev > b_lev:
        temp = a
        a = b
        b = temp
    b_len = abs(b_lev - a_lev)
    for _ in range(b_len):
        b = find_parent(b)
    while a != b:
        a, b = find_parent(a), find_parent(b)
        a_len += 1
        b_len += 1
    print(a_len + b_len)
