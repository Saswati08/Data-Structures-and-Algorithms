def minimax(arr, low, high):
    if low == high:
        return arr[low], arr[high]
    elif low == high - 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    else:
        mid = (low + high)//2
        leftmin, leftmax = minimax(arr, low, mid)
        rightmin, rightmax = minimax(arr, mid+1, high)
        if leftmin < rightmin:
            mini = leftmin
        else:
            mini = rightmin
        if leftmax > rightmax:
            maxi = leftmax
        else:
            maxi = rightmax
        return mini, maxi
        
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    minm, maxm = minimax(arr, 0, n - 1)
    print(str(minm) +" "+ str(maxm))
    m += 1

