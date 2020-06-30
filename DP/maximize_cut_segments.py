def maximizeTheCuts(n,x,y,z):
    
    #returns: max number cuts.
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0
    cut_segs = [x, y, z]
    for cuts in cut_segs:
        for j in range(1, n + 1):
            
            if j >= cuts and dp[j - cuts] != '-inf':
                dp[j] = max(dp[j], dp[j - cuts] + 1)
    # print(dp) 
    if dp[n] <= 0:
        return 0
    if dp[j] != '-inf':
        return dp[n]
    

print(maximizeTheCuts(16, 1, 3, 5))

