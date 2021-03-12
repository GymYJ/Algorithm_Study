import sys


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def main():
    n = int(sys.stdin.readline())
    tree = {}
    for _ in range(n):
        node, left, right = sys.stdin.readline().split()
        tree[node] = Node(node, left, right)

    def preorder(node_):
        nonlocal tree
        print(node_.data, end='')
        if node_.left != '.':
            preorder(tree[node_.left])
        if node_.right != '.':
            preorder(tree[node_.right])

    def inorder(node_):
        nonlocal tree
        if node_.left != '.':
            inorder(tree[node_.left])
        print(node_.data, end='')
        if node_.right != '.':
            inorder(tree[node_.right])

    def postorder(node_):
        nonlocal tree
        if node_.left != '.':
            postorder(tree[node_.left])
        if node_.right != '.':
            postorder(tree[node_.right])
        print(node_.data, end='')

    preorder(tree['A'])
    print('')
    inorder(tree['A'])
    print('')
    postorder(tree['A'])


if __name__ == '__main__':
    main()
