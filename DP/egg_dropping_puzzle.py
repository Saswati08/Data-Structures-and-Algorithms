t = int(input())
m = 0
while(m < t):
    n, k = map(int, input().strip().split())
    dp = [[float('inf')] * (k + 1) for i in range(n + 1)]
    for i in range(1, k + 1):
        dp[1][i] = i
        
    for i in range(0, n + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    # for i in range(0, k + 1):
    #     dp[0][i] = 0
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            # res = float('inf')
            # dp[i][j] = float('inf')
            for floors in range(1, j):
                temp = 1 + max(dp[i - 1][floors - 1], dp[i][j - floors])
                dp[i][j] = min(temp, dp[i][j])
                
    print(dp[n][k])
                
    m += 1
