import sys

n, d, k, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
answer = 0
pick = [0 for _ in range(d + 1)]
count = 0
coupon = 0
for i in range(n - 1, n - k - 1, -1):
    num = arr[i]
    if num == c:
        coupon += 1
    if pick[num] == 0:
        count += 1
    pick[num] += 1
if coupon == 0:
    answer = count + 1
else:
    answer = count
for i in range(n - k - 1, -k, -1):
    delete = arr[i + k]
    if delete == c:
        coupon -= 1
    pick[delete] -= 1
    if pick[delete] == 0:
        count -= 1
    num = arr[i]
    if num == c:
        coupon += 1
    if pick[num] == 0:
        count += 1
    pick[num] += 1
    if coupon == 0 and answer < count + 1:
        answer = count + 1
    elif coupon != 0 and answer < count:
        answer = count
print(answer)
