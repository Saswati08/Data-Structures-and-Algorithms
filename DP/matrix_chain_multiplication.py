t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    dp = [[0 for j in range(n)] for i in range(n)]
    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                temp = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                if dp[i][j] > temp:
                    dp[i][j] = temp
    print(dp[0][n - 1])
    m += 1
