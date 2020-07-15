class LRUCache:
        
    def __init__(self,cap):
        # cap:  capacity of cache
        #Intialize all variable
        #code here
        self.size = cap
        self.map = {}
        self.queue = []
        
    
    #This method works in O(1)
    def get(self, key):
        #code here
        if key in self.map:
            x = self.map[key]
            self.queue.remove(key)
            self.queue.append(key)
            return x
        else:
            return -1
        
        
    #This method works in O(1)   
    def set(self, key, value):
        #code here
        if key in self.map:
            self.map[key] = value
            self.queue.remove(key)
            self.queue.append(key)
            
        else:
            if len(self.queue) == self.size:
                front = self.queue.pop(0)
                self.map.pop(front)
            self.queue.append(key)
            self.map[key] = value
            
            





#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends
