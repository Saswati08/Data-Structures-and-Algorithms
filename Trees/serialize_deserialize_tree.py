

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def serialize(root, A):
    queue = [root]
    A.append(root.data)
    while(queue):
        front = queue.pop(0)
        if front.left:
            queue.append(front.left)
            A.append(front.left.data)
        else:
            A.append(-1)
        if front.right:
            queue.append(front.right)
            A.append(front.right.data)
        else:
            A.append(-1)
   

def deSerialize(A):
    # print(A)
    
    
    root = Node(A[0])
    queue = [root]
    i = 1
    while(queue and i < len(A)):
        front = queue.pop(0)
        if A[i] != -1:
            # print(A[i], end ="")
            front.left = Node(A[i])
            queue.append(front.left)
        i += 1
        if i >= len(A):
            break
        if A[i] != -1:
            front.right = Node(A[i])
            queue.append(front.right)
        i += 1
    return root
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Suman Rana
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        A=[]
        serialize(root, A)
        r=deSerialize(A)
        inorder(r)
        print()
        

# } Driver Code Ends
