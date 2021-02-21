def main():
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    loc = [[(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (-1, 2)], [(0, 1), (1, 1), (2, 1)], [(-1, 0), (-1, 1), (-1, 2)],
           [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], [(0, 1), (-1, 1), (-2, 1)], [(0, 1), (0, 2), (1, 2)],
           [(-1, 0), (-2, 0), (-2, 1)], [(1, 0), (1, 1), (1, 2)], [(1, 0), (0, 1), (1, 1)], [(1, 0), (1, 1), (2, 1)],
           [(0, 1), (-1, 1), (-1, 2)], [(-1, 0), (-1, 1), (-2, 1)], [(0, 1), (1, 1), (1, 2)], [(-1, 1), (0, 1), (1, 1)],
           [(1, 0), (1, 1), (2, 0)], [(0, 1), (-1, 1), (0, 2)], [(0, 1), (1, 1), (0, 2)]]
    biggest = 0
    for i in range(n):
        for j in range(m):
            for li in loc:
                num = arr[i][j]
                can = True
                for x, y in li:
                    if 0 <= i + x < n and 0 <= j + y < m:
                        num += arr[i + x][j + y]
                    else:
                        can = False
                if can and num > biggest:
                    biggest = num
    print(biggest)


if __name__ == '__main__':
    main()
