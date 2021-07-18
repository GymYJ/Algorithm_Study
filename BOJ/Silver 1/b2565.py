import sys

N = int(sys.stdin.readline())
line = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 기본 LIS문제와 다른 점, 정렬한 후 다른 전봇대를 보는 것
line.sort()

dp = [0] * N
# 이 부분을 안해도 Test Case에서는 정답이 나오지만
# 몇 가지 반례에서 다른 답이 나온다.
dp[0] = 1
# 다른건 기본 LIS의 아이디어를 활용함.
for i in range(1, N):
    min_value = 0
    for j in range(i):
        if line[i][1] > line[j][1]:
            min_value = max(dp[j], min_value)
    dp[i] = min_value + 1
print(N - max(dp))
