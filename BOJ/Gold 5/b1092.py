import sys
from collections import deque

n = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()
boxes = deque(boxes)
count = 0
while boxes:
    count += 1
    new_boxes = []
    for c in cranes:
        if boxes:
            while boxes:
                b = boxes.popleft()
                if c >= b:
                    break
                new_boxes.append(b)
        else:
            break
    boxes = deque(new_boxes + list(boxes))
print(count)
