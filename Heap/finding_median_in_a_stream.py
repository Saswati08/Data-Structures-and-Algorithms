def balanceHeaps():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    Balance the two heaps size , such that difference is not more than one.
    '''
    # code here
    global min_heap
    global max_heap
    if len(max_heap) - len(min_heap) >= 2:
        heapq.heappush(min_heap,(heapq.heappop(max_heap)) * -1)
        
    elif len(min_heap) - len(max_heap) >= 2:
        heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
    
def getMedian():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :return: return the median of the data received till now.
    '''
    # code here
    global min_heap
    global max_heap
    if len(min_heap) == len(max_heap):
        return (max_heap[0] * -1 + min_heap[0])//2
    else:
        if len(min_heap) > len(max_heap):
            return min_heap[0]
        else:
            return max_heap[0] * -1
    
def insertHeaps(x):
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :param x: value to be inserted
    :return: None
    '''
    # code here
    global min_heap
    global max_heap
    if len(max_heap) == 0 or x < max_heap[0] * -1:
        heapq.heappush(max_heap, x * -1)
    else:
        heapq.heappush(min_heap, x)
        
    # print(max_heap, min_heap)

min_heap = []
max_heap = []
n = int(input())
for i in range(n):
	insertHeaps(int(input()))
	balanceHeaps()
	print(getMedian())
