def heapify(ind):
    global curr_size
    left = ind * 2 + 1
    right = ind * 2 + 2
    smallest = ind
    if left < curr_size and heap[left] < heap[ind]:
        smallest = left
        
    if right < curr_size and heap[right] < heap[smallest]:
        smallest = right
        
    if smallest != ind:
        heap[smallest], heap[ind] = heap[ind], heap[smallest], 
        heapify(smallest)
        
def insertKey (x):
    '''
    :param x: Insert value in heap.
    :return: None
    '''
    global curr_size
    heap[curr_size] = x
    ind = curr_size
    curr_size += 1
    
    p = (ind - 1)//2
    while(heap[p] > heap[ind] and p >= 0):
        heap[p], heap[ind] = heap[ind], heap[p]
        ind = p
        p = (ind - 1)//2

def decreaseKey(x, val):
    heap[x] = val
    p = (x - 1)//2
    while(p >= 0 and heap[p] > heap[x]):
        heap[p], heap[x] = heap[x], heap[p]
        x = p
        p = (x - 1)//2
    

def deleteKey(x):
    '''
    :param x: Index of value to be removed from heap.
    :return: None
    '''
    global curr_size
    if x >= curr_size or curr_size == 0:
        return 
    decreaseKey(x, float('-inf'))
    extractMin()
    
    


def extractMin():
    global curr_size
    if curr_size == 0:
        return -1
    front = heap[0]
    heap[0] = heap[curr_size - 1]
    curr_size -= 1
    heapify(0)
    return front

heap = []
curr_size = 0

insertKey(1)
insertKey(2)
insertKey(3)
insertKey(4)
decreaseKey(2, 2)
deleteKey(1)
extractMin()
