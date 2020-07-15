t = int(input())
m = 0
while(m < t):
    r, c = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    M = [[0 for i in range(c)] for i in range(r)]  
    # print(arr)
    x = 0
    queue = []
    
    levels = 0
    for i in range(r):
        for j in range(c):
            M[i][j] = arr[x]
            if M[i][j] == 2:
                queue.append((i, j))
            x += 1
                
                
            
        
    # print(queue)
    while(queue):
        q_len = len(queue)
        x = 0
        while(x < q_len):
            # print(M)
            i, j = queue.pop(0)
            
            if i != 0 and M[i - 1][j] == 1:
                M[i - 1][j] = 2
                queue.append((i - 1, j))
            if i != r - 1 and M[i + 1][j] == 1:
                M[i + 1][j] = 2
                queue.append((i + 1, j))
            if j != 0 and M[i][ j - 1] == 1:
                M[i][j - 1] = 2
                queue.append((i, j - 1))
            if j != c - 1 and M[i][j + 1] == 1:
                M[i][j + 1] = 2
                queue.append((i, j + 1))
                
            x += 1
        levels += 1
    # print(M)
    flag = 0
    for i in range(r):
        for j in range(c):
            if M[i][j] == 1:
                flag = -1
    if flag == -1:
        print(flag)
    else:
        print(levels - 1)
            
    m += 1
