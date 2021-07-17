import sys


class Node:
    def __init__(self, made):
        self.made = made
        self.recommend = 1


class Pictures:
    def __init__(self, maxsize):
        self.pictures = {}
        self.maxsize = maxsize
        self.size = 0

    def recommend(self, num, time):
        if num in self.pictures:
            self.pictures[num].recommend += 1
        else:
            if self.size == self.maxsize:
                self.delete()
                self.size -= 1
            self.pictures[num] = Node(time)
            self.size += 1

    def delete(self):
        min_rec = 1001
        for pic in self.pictures:
            if self.pictures[pic].recommend < min_rec:
                min_rec = self.pictures[pic].recommend
        made = 1001
        target = 0
        for pic in self.pictures:
            if self.pictures[pic].recommend == min_rec and self.pictures[pic].made < made:
                target = pic
                made = self.pictures[pic].made
        self.pictures.pop(target)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
p1 = Pictures(n)
for i, num in enumerate(arr):
    p1.recommend(num, i)
print(' '.join(list(map(str, sorted(list(p1.pictures.keys()))))))
