t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    jumps = 1
    maxreach = arr[0]
    steps = arr[0]
    flag = 0
    if arr[0] == 0:
        print(-1)
    else:
        i = 1
        while(i < n - 1):
            
            
            maxreach = max(maxreach, arr[i] + i)
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = maxreach - i
                if maxreach <= i:
                    flag = -1
                    
                
            
            i += 1
            
        if flag == -1:
            print(-1)
        else:
            print(jumps)
    m += 1
        
