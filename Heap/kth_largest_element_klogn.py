from heapq import heappush, heappop, heapify
def kthLargest(a,n,k):
    '''
    :param a: given array
    :param n: size of array
    :param k: value of k
    :return: Integer.
    '''
    # code here
    heap = []
    
        
    for i in range(n):
        heappush(heap, a[i])
        
    for i in range(n - k):
        
        # print(i, heappop(heap))
        heappop(heap)
        
    return heappop(heap)
    
    
print(kthLargest([2, 9, 8, 6, 4, 3], 6, 3))
