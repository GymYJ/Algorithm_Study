from collections import deque


def main():
    n = int(input())
    shark = ()
    arr = []
    for i in range(n):
        row = list(map(int, input().split()))
        if 9 in row:
            shark = (i, row.index(9))
        arr.append(row)
    seconds = 0
    move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    can = True
    size = 2
    count = 0
    arr[shark[0]][shark[1]] = 0
    while can:
        q = deque([(shark, 0)])
        visit = [shark]
        target = (n, n)
        leng = n ** 2
        while q:
            now, now_leng = q.popleft()
            if 0 < arr[now[0]][now[1]] < size and now_leng <= leng:
                if now[0] < target[0]:
                    target = now
                    leng = now_leng
                elif now[0] == target[0]:
                    if now[1] < target[1]:
                        target = now
                        leng = now_leng
                continue
            for x, y in move:
                if 0 <= now[0] + x < n and 0 <= now[1] + y < n:
                    if arr[now[0] + x][now[1] + y] <= size and (now[0] + x, now[1] + y) not in visit:
                        q.append(((now[0] + x, now[1] + y), now_leng + 1))
                        visit.append((now[0] + x, now[1] + y))
        if target == (n, n):
            break
        else:
            seconds += leng
            arr[target[0]][target[1]] = 0
            shark = target
            count += 1
            if size == count:
                size += 1
                count = 0
    print(seconds)


if __name__ == '__main__':
    main()
