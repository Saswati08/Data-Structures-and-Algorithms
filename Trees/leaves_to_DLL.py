class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def convDLL(root):
    if root == None:
        return 
    elif root.left == None and root.right == None:
        
        root.right = convDLL.hd
        
        if convDLL.hd != None:
            convDLL.hd.left = root
            
        
        convDLL.hd = root
        return None
        
    root.right = convDLL(root.right)
    root.left = convDLL(root.left)
    return root
    
def convertToDLL(root):
    #return the head of the DLL and remove those node from the tree as well.
    convDLL.hd = None
    root = convDLL(root)
    return convDLL.hd

def printInorder(root): 
    if root is not None: 
        printInorder(root.left) 
        print root.data, 
        printInorder(root.right) 
  
  
def printList(head): 
    while(head): 
        if head.data is not None: 
            print head.data, 
        head = head.right 
  


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(6) 
root.left.left.left = Node(7) 
root.left.left.right = Node(8) 
root.right.right.left = Node(9) 
root.right.right.right = Node(10) 
  
print "Inorder traversal of given tree is:"
printInorder(root) 
  
root = extractLeafList(root) 
  
print "\nExtract Double Linked List is:"
printList(convertToDLL.head) 
  
print "\nInorder traversal of modified tree is:"
printInorder(root) 
