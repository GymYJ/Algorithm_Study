import sys

sys.setrecursionlimit(100000)


# 4 2 5 1 6 3 7
# 4 5 2 6 7 3 1
# 1 2 4 5 3 6 7
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    answer.append(str(node.data))
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


def make_node(r, ios, ioe, pos, poe):
    io_index = inorder.index(r.data)
    if io_index != ios and ioe - ios > 0:
        if ioe > io_index:
            po_index = postorder.index(inorder[io_index + 1])
        else:
            po_index = postorder.index(r.data)
        left = Node(postorder[po_index - 1])
        r.left = left
        make_node(left, ios, io_index - 1, pos, po_index - 1)
    if ioe > io_index:
        if postorder.index(r.data) != poe:
            po_index = postorder.index(inorder[io_index + 1])
        else:
            po_index = pos
        right = Node(postorder[poe - 1])
        r.right = right
        make_node(right, io_index + 1, ioe, po_index, poe - 1)


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
root = Node(postorder[-1])
make_node(root, 0, n - 1, 0, n - 1)
answer = []
preorder(root)
print(' '.join(answer))
