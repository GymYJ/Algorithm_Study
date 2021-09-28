import sys


def inorder(no, lev):
    global node, node_col_level, seq, width
    left, right = node[no]
    if left != -1:
        inorder(left, lev + 1)

    seq += [no]
    if width[lev] == [0, 0]:
        width[lev] = [len(seq), len(seq)]
    else:
        if width[lev][0] > len(seq):
            width[lev][0] = len(seq)
        if width[lev][1] < len(seq):
            width[lev][1] = len(seq)

    if right != -1:
        inorder(right, lev + 1)


n = int(sys.stdin.readline())
node = [[] for _ in range(n + 1)]
check = [0 for _ in range(n + 1)]
check[0] = 1
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if b != -1:
        check[b] = 1
    if c != -1:
        check[c] = 1
    node[a] = [b, c]
root = check.index(0)
node_col_level = [[0, 0] for _ in range(n + 1)]
width = [[0, 0] for _ in range(n + 1)]
seq = []
inorder(root, 1)

answer = [0, 0]
for i in range(1, n + 1):
    if width[i] == [0, 0]:
        break
    left, right = width[i]
    if answer[1] < right - left + 1:
        answer = [i, right - left + 1]
print(*answer)
