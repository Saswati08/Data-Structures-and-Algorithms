def minDist(arr, n, x, y):
    # Code here
    xi = -1
    yi = -1
    d = n
    for i in range(0, n):
        if arr[i] == x:
            xi = i
        if arr[i] == y:
            yi = i
        if (xi == i or yi == i) and (xi != -1 and yi != -1):
            d = min(d, abs(yi - xi))
    if xi == -1 or yi == -1:
        return -1
    return d
    
  
    


