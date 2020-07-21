# Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    # leftmin = [0]
    # minm = arr[0]
    # mini = 0
    # for i in range(1, n):
        
    #     if arr[i] < minm:
            
    #         minm = arr[i]
    #         mini = i
    #     leftmin.append(mini)
    # print(leftmin)
    # rightmax = [0 for i in range(n)]
    # maxi = n - 1
    # maxm = arr[n - 1]
    # for i in range(n - 1, -1, -1):
        
    #     if arr[i] > maxm:
            
    #         maxm = arr[i]
    #         maxi = i
    #     rightmax[i] = maxi
    # print(rightmax)
    # maxm_ind = 0
    maxDiff = 0; 
    LMin = [0] * n 
    RMax = [0] * n 
  
    # Construct LMin[] such that  
    # LMin[i] stores the minimum  
    # value from (arr[0], arr[1],  
    # ... arr[i])  
    LMin[0] = arr[0] 
    for i in range(1, n): 
        LMin[i] = min(arr[i], LMin[i - 1]) 
  
    # Construct RMax[] such that  
    # RMax[j] stores the maximum  
    # value from (arr[j], arr[j+1], 
    # ..arr[n-1])  
    RMax[n - 1] = arr[n - 1] 
    for j in range(n - 2, -1, -1): 
        RMax[j] = max(arr[j], RMax[j + 1]); 
  
    # Traverse both arrays from left 
    # to right to find optimum j - i 
    # This process is similar to 
    # merge() of MergeSort 
    i, j = 0, 0
    maxDiff = 0
    while (j < n and i < n): 
        if (LMin[i] < RMax[j]): 
            maxDiff = max(maxDiff, j - i) 
            j = j + 1
        else: 
            i = i+1
    print(maxDiff)
    m += 1
