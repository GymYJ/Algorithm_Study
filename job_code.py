from collections import Counter, deque, defaultdict
import heapq
from itertools import permutations, combinations, product
import datetime


def add_1(num):
    return num + 1


a = [2, 1, 3, 4]
print(a)
a.insert(6, 1)
print(a)
heapq.heapify(a)  # min heap 임
print(a)
a = list(map(add_1, a))
print(a)
a = list(map(lambda x, y=1: x + 1, a))
print(a)
counter = Counter(a)
print((counter))
print(counter[1], counter[2])
print(sum(counter))

b = deque([1, 2, 3])
print(b.popleft())
print(b.pop())

c = {1, 2, 3}
c.add(3)
print(c)

c = 'a' * 4
print(c)

d = defaultdict(list)
d['12'].append(123)
d['1'] = [1]
for i in d:
    print(i)

a = '23'
a.startswith('1')
print(a.startswith('1'))

a = 'abbc'
for i in permutations(a, 2):
    print(i)

print(bin(9 | 20))

a = [1, 2, 3]
for i, j in permutations(a, 2):
    print(i, j)
print('-----')
for i, j in combinations(a, 2):
    print(i, j)
a = 5
print(bin(a))
print(bin(a >> 1))
print(bin(a << 1))
a = bin(a)
print(a[2:])
a = [1, 2]
a[1] += 1
print(a)
a = '123'
print(a.isdigit())
a = 'abc'
print(a.isalpha())
a = 'a가1'
print(a.isalnum())
a = deque([], maxlen=3)
for i in range(5):
    a.append(i)
    print(a)

b = datetime.datetime.strptime('12:30', '%H:%M')
print(str(b.hour) + ':' + str(b.minute))

aaa = 'a'


def sol():
    aaa = 1
    bbb = []
    ccc = {}

    def si(x):
        nonlocal aaa
        aaa = aaa + 1
        bbb.append(x)
        ccc[x] = x

    si('a')
    si('b')
    si('c')
    print(aaa, bbb, ccc)


sol()

a = '123'
print(a[-1])