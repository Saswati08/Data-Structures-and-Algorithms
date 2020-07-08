def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    # code here
    left = i * 2 + 1
    right = i * 2 + 2
    maxi = i
    if left < n and arr[left] > arr[maxi]:
        maxi = left
    if right < n and arr[right] > arr[maxi]:
        maxi = right
    if maxi != i:
        arr[maxi], arr[i] = arr[i], arr[maxi]
        heapify(arr, n, maxi)

def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    # code here
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = map(int, input().strip().split())
