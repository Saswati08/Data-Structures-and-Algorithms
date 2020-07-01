t = int(input())
m = 0
while(m < t):
    string = input()
    n = len(string)
    dp =[[0] * n for i in range(n)]
    maxm = -1
    st = 0
    f = 0
    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n - 1):
        if string[i] == string[i + 1]:
            dp[i][i + 1] = 2
            if maxm < 2:
                maxm = 2
                st = i
                f = i + 1
            
        
    
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if string[i] == string[j] and dp[i + 1][j - 1] >= 1:
                dp[i][j] = dp[i + 1][j - 1] + 2
                if maxm < k:
                    st = i
                    f = j
                    maxm = k
    print(string[st : f + 1])
        
    m += 1
