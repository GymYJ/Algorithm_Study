import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor = list(set(list(map(int, sys.stdin.readline().split()))))
sensor.sort()
distance = []
before = sensor[0]
for now in sensor[1:]:
    distance.append(now - before)
    before = now
distance.sort()
while distance and k > 1:
    distance.pop()
    k -= 1
print(sum(distance))
