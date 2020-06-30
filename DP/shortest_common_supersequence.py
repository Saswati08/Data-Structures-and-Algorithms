t = int(input())
m = 0
while(m < t):
    str1, str2 = input().strip().split(" ")
    
    dp = [[0] * (len(str1) + 1) for i in range(len(str2) + 1)]
    # print(len(dp), len(dp[0]))
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i- 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # print(dp[i][j], i, j)
    print(len(str1) + len(str2) - dp[i][j])
    m += 1
