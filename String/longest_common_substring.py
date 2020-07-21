t = int(input())
x = 0
while(x < t):
    n, m = map(int, input().strip().split())
    str1 = input()
    str2 = input()
    dp = [[0] * (m + 1) for i in range(n + 1)]
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    # print(dp)
    print(res)
