import sys


def toPostorder(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return

    root_idx = inorder.index(preorder[0])

    left_in = inorder[0:root_idx]
    left_pre = preorder[1:len(left_in) + 1]
    toPostorder(left_pre, left_in)

    right_in = inorder[root_idx + 1:]
    right_pre = preorder[len(left_pre) + 1:]
    toPostorder(right_pre, right_in)

    print(preorder[0], end=' ')


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    preo = list(map(int, sys.stdin.readline().split()))
    ino = list(map(int, sys.stdin.readline().split()))

    toPostorder(preo, ino)
    print()