t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    dp = [0] * n
    dp[0] = arr[0]
    s = arr[0]
    for i in range(1, n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i] 
                s = max(dp[i], s)
            
    print(s)
    m += 1
