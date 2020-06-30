#Given a A X B matrix with your initial position at the top-left cell, find the number of possible unique paths to reach the bottom-right cell of the matrix from the initial position.

#Note: Possible moves can be either down or right at any point in time, i.e., we can move to matrix[i+1][j] or matrix[i][j+1] from matrix[i][j].
def NumberOfPaths(a, b):
    #code here
    
    # count = count_path(a, b, 0, 0)
    dp = [[0] * b for i in range(a)]
    for i in range(b):
        dp[0][i] = 1
    for i in range(a):
        dp[i][0] = 1
    for i in range(1, a):
        for j in range(1, b):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[a - 1][b - 1]

print(NumberOfPaths(4, 6))
    

