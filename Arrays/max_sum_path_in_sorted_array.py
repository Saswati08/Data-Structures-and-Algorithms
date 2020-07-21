def maxSumPath(arr1, arr2, m, n):
    #code here
    p = 0
    q = 0
    s1 = 0
    s2 = 0
    result = 0
    while(p < m and q < n):
       
    #   if arr1[p] < arr2[q]:
    #       s1 += arr1[p]
    #       p += 1
        if arr1[p] < arr2[q]:
            s1 += arr1[p]
            p += 1
            
        elif arr2[q] < arr1[p]:
            s2 += arr2[q]
            q += 1
            
        else:
            result += max(s1, s2) + arr1[p]
            s1 = 0
            s2 = 0
            p += 1
            q += 1
        
    while(p < m):
        s1 += arr1[p]
        p += 1
    
    while(q < n):
        s2 += arr2[q]
        q += 1
        
    result += max(s1, s2)
    return result
       

