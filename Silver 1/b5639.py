import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def main():
    root = Node(int(input()))
    while True:
        try:
            num = int(input())
        except EOFError:
            break
        node = root
        while True:
            if node.data > num:
                if node.left is None:
                    node.left = Node(num)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(num)
                    break
                else:
                    node = node.right

    def postorder(node_):
        if node_.left is not None:
            postorder(node_.left)
        if node_.right is not None:
            postorder(node_.right)
        print(node_.data)

    postorder(root)


if __name__ == '__main__':
    main()
