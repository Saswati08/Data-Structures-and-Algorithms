t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    dp = [[0 for j in range(n)] for i in range(n)]
    for k in range(0, n):
        for j in range(k, n):
            i = j - k
            x = 0
            if i  + 2 <= j:
                x = dp[i + 2][j]
            y = 0
            if i + 1 <= j - 1:
                y = dp[i + 1][j - 1]
            z = 0
            if i <= j - 2:
                z = dp[i][j - 2]
            dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
    print(dp[0][n - 1])
    m += 1
