#Given an array, the task is to divide it into two sets S1 and S2 such that the absolute #difference between their sums is minimum.
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    s = 0
    for i in range(n):
        s += arr[i]
    arr_sum = s
    s = s//2
    dp = [[False] * (s + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    # print(arr_sum, s)
    diff = float('inf')
    for i in range(s, 0, -1):
        if dp[n][i] == True:
            # print(i)
            diff = arr_sum - 2 * i
            break
    print(diff)
    m += 1
