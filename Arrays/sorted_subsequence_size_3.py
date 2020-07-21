def find3number(A, n):
    # code here
    minm = A[0]
    mini = 0
    left = []
    left.append(-1)
    for i in range(1, n):
        if A[i] > minm:
            left.append(mini)
        else:
            left.append(-1)
            if A[i] < minm:
                minm = A[i]
                mini = i
    right = []
    right.append(-1)
    maxm = A[n - 1]
    maxi = n - 1
    for i in range(n - 2, -1, -1):
        if A[i] < maxm:
            right.append(maxi)
        else:
            right.append(-1)
            if A[i] > maxm:
                maxm  = A[i]
                maxi = i
                
    for i in range(n//2):
        temp = right[i]
        right[i] = right[n - 1 - i]
        right[n - 1 - i] = temp
    
    for i in range(n):
        if left[i] != -1 and right[i] != -1:
            return [A[left[i]], A[i], A[right[i]]]
    return []

