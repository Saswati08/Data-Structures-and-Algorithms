def minCost(a,n) :
    '''
    use heapq module , imported already by driver code.
    :param a: given array
    :param n: size of array
    :return: Integer
    '''
    # code here
    heap = a[:]
    heapq.heapify(heap)
    # print(heap)
    cost = 0    
    while(len(heap) > 1):
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        cost += min1 + min2
        # print(cost)
        heapq.heappush(heap, min1 + min2)
        # print(heap)
        
    return cost

a = [5, 6, 2, 4]
n = 4
print(minCost(a, n))
