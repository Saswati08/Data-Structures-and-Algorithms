def histogram(arr, n):
    max_area = float('-inf')
    stack = []
    i = 0
    while(i < n):
        if not stack or arr[stack[-1]] <= arr[i]:
            stack.append(i)
            i += 1
        else:
            while(stack and arr[stack[-1]] > arr[i]):
                top = arr[stack.pop(-1)]
                if stack:
                    area = top * (i - stack[-1] - 1)
                else:
                    area = top * i
                max_area = max(max_area, area)
            
    while(stack):
        top = arr[stack.pop(-1)]
        if stack:
            area = top * (i - stack[-1] - 1)
        else:
            area = top * i
        max_area = max(area, max_area)
    return max_area
                

def maxRectangle(M, n, m):
    # code here
    
    for i in range(1, n):
        nw_his = []
        for j in range(0, m):
            if M[i][j] == 1:
                nw_his.append(M[i][j] + M[i - 1][j])
            else:
                nw_his.append(0)
        M[i] = nw_his
        
    # print(M)
        
    max_area = histogram(M[0], m)
    for i in range(1, n):
        max_area = max(max_area, histogram(M[i], m))
        
    return max_area


M = [[0, 1, 1, 0], [1, 1, ,1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
n = 4
m = 4
print(maxRectangle(M, n, m))
