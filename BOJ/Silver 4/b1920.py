n = input()
a = list(map(int, input().split(' ')))
a.sort()
m = int(input())
m_list = list(map(int, input().split(' ')))
answer = []
for i in range(m):
    left, right = 0, len(a) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == m_list[i]:
            break
        elif a[mid] > m_list[i]:
            right = mid - 1
        else:
            left = mid + 1
    if a[mid] == m_list[i]:
        answer.append(1)
    else:
        answer.append(0)
for i in answer:
    print(i)
