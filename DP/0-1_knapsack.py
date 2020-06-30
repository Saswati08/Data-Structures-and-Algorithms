def knapSack(W, wt, val, n):
    '''
    :param W: capacity of knapsack 
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    '''
    # code here
    dp = [ [0]* (W + 1) for _ in range(n + 1)]
    # for i in range(n + 1):
    #     dp[0][i] = 0
    # for i in range(W + 1):
    #     dp[0][i] = 0
        
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j < wt[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
    # print(dp)
    return dp[n][W]


print(knapSack(4, [1, 2, 3], [4, 5, 1], 3))
