t = int(input())
m = 0
while(m < t):
    st = input()
    n = len(st)
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    rev = "".join(reversed(st))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if st[i - 1] == rev[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[n][n]
    print(n - lcs)
    m += 1
