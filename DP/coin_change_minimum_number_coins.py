def minimumNumberOfCoins(coins,n,value):
    
    # your code here
    dp = [float('inf')] * (value + 1)
    dp[0] = 0
    for i in coins:
        for j in range(1, value + 1):
            if j >= i:
                dp[j] = min(dp[j], dp[j - i] + 1)
                
    # print(dp)
    if dp[value] == float('inf'):
        return -1
    else:
        return dp[value]

print(miniNumberOfCoins([1, 3, 5], 3, 10))

