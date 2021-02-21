from itertools import combinations
from math import inf


def main():
    n, m = list(map(int, input().split()))
    chicken = []
    house = []
    for i in range(n):
        row = list(map(int, input().split()))
        for j, r in enumerate(row):
            if r == 2:
                chicken.append((i, j))
            elif r == 1:
                house.append((i, j))
    smallest = inf
    for c in combinations(chicken, m):
        dp = [inf for _ in range(len(house))]
        for cx, cy in c:
            for i, h in enumerate(house):
                hx, hy = h
                if abs(cx - hx) + abs(cy - hy) < dp[i]:
                    dp[i] = abs(cx - hx) + abs(cy - hy)
        if smallest > sum(dp):
            smallest = sum(dp)
    print(smallest)


if __name__ == '__main__':
    main()
