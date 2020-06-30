#Given a N X N  matrix Matrix[N][N] of positive integers.  There are only three possible moves from a cell Matrix[r][c].

#1. Matrix[r+1][c]

#2. Matrix[r+1][c-1]

#3. Matrix[r+1][c+1]

#Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    x = 0
    mat = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(arr[x])
            x += 1
        mat.append(temp)
    # print(mat)
    dp = [[0] * n for i in range(n)]
    result = 0
    for i in range(n):
        dp[0][i] = mat[0][i]
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1]) + mat[i][j]
            elif j == n - 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + mat[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], max(dp[i - 1][j - 1], dp[i - 1][j + 1])) + mat[i][j]
            if i == n - 1:
                result = max(result, dp[i][j])
    print(result)
    m += 1
