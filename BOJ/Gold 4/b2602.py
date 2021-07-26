import sys

paper = [''] + list(sys.stdin.readline().strip())
bridge = []
for _ in range(2):
    bridge.append([''] + list(sys.stdin.readline().strip()))
dp1 = [[0 for _ in range(len(bridge[0]))] for _ in range(len(paper))]
for i in range(1, len(paper)):
    for j in range(1, len(bridge[0])):
        if i == 1:
            dp1[i][j] = dp1[i][j - 1]
            if bridge[0][j] == paper[i]:
                dp1[i][j] += 1
        else:
            if i % 2 == 1:
                dp1[i][j] = dp1[i][j - 1]
                if bridge[0][j] == paper[i]:
                    dp1[i][j] += dp1[i - 1][j - 1]
            else:
                dp1[i][j] = dp1[i][j - 1]
                if bridge[1][j] == paper[i]:
                    dp1[i][j] += dp1[i - 1][j - 1]
dp2 = [[0 for _ in range(len(bridge[0]))] for _ in range(len(paper))]
for i in range(1, len(paper)):
    for j in range(1, len(bridge[0])):
        if i == 1:
            dp2[i][j] = dp2[i][j - 1]
            if bridge[1][j] == paper[i]:
                dp2[i][j] += 1
        else:
            if i % 2 == 1:
                dp2[i][j] = dp2[i][j - 1]
                if bridge[1][j] == paper[i]:
                    dp2[i][j] += dp2[i - 1][j - 1]
            else:
                dp2[i][j] = dp2[i][j - 1]
                if bridge[0][j] == paper[i]:
                    dp2[i][j] += dp2[i - 1][j - 1]
print(dp1[-1][-1] + dp2[-1][-1])
