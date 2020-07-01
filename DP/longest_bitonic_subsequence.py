t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = [1] * n
    lds = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    
    result = 0
    for i in range(n):
        result = max(result, lis[i] + lds[i] -1)
    print(result)
    m += 1
