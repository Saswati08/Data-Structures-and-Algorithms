t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    s = 0
    for i in arr:
        s += i
    if s % 2 != 0:
        print("NO")
    
    
    else:
         s = s//2
        dp = [[False] * (s + 1) for i in range(n + 1)]
        for i in range(0, n + 1):
           dp[i][0] = True
        for i in range(1, n + 1):
             for j in range(1, s + 1):
                if j >= arr[i - 1]:
                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
             else:
                 dp[i][j] = dp[i - 1][j]
        if dp[n][s]:
             print("YES")
         else:
             print("NO")
        # if isSubsetSum(arr, n, int(s/2)):
        #     print("YES")
        # else:
        #     print("NO")
    m += 1
