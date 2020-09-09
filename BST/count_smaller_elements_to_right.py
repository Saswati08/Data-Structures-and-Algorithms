class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.freq = 1
        self.lcount = 0

def insert(root, x):
    curr = root
    count = 0
    while(curr != None):
        prev = curr
        
        if x < curr.value:
            curr.lcount += 1
            curr = curr.left
        elif x > curr.value:
            count += curr.lcount + curr.freq
            curr = curr.right
        else:
            prev = curr
            curr.freq += 1
            break
        
    if prev.value < x:
        prev.right = Node(x)
        
    elif prev.value > x:
        prev.left = Node(x)
        
    else: count += prev.lcount
    return count
            
    
    
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    smaller = [0] * n
    root = Node(arr[n - 1])
    for i in range(n - 2, -1, -1):
        smaller[i] = insert(root, arr[i])
    # print(smaller)
    for i in smaller:
        print(i, end = " ")
    print()
        
    m += 1
