t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    dp = [1] * n

    result = 0
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        result = max(dp[i], result)
        
    print(result)
    m += 1
