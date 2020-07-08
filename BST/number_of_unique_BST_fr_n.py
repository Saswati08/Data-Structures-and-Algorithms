#2nCn * 1/(n + 1) also can be done

t = int(input())
m = 0
while(m < t):
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        
        for j in range(1, i + 1):
            dp[i] += dp[i - j] * dp[j - 1]
            
    print(dp[n])
    m += 1
