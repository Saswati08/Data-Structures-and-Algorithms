def calculateSpan(a,n):
    #code here
    stack = [0]
    span = [1] * n
    for i in range(1, n):
        
        
            
        while(stack and a[stack[-1]] <= a[i]):
            ind = stack.pop(-1)
            span[i] += span[ind]
        
        stack.append(i)
            
    return span
            

print(calculateSpan([100 80 60 70 60 75 85], n))
