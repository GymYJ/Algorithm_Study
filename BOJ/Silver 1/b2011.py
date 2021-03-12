code = list(input())
dp = [0 for _ in range(len(code) + 1)]
dp[1] = 1 if code[0] != '0' else 0
if len(code) >= 2:
    if code[1] != '0':
        dp[2] += dp[1]
    if code[0] == '1' or code[0] == '2':
        temp = int(code[0] + code[1])
        if 10 <= temp <= 26:
            dp[2] += 1
    before = code[1]
    for i, n in enumerate(code[2:], start=3):
        now = n
        if now != '0':
            dp[i] += dp[i - 1]
        if before == '1' or before == '2':
            temp = int(before + now)
            if 10 <= temp <= 26:
                dp[i] += dp[i - 2]
        before = now
print(dp[-1] % 1000000)
