def level(x, root, l):
    if root == None:
        return 
    if root.data == x:
        return l
    if level(x, root.left, l + 1):
        return level(x, root.left, l + 1)
    if level(x, root.right, l + 1):
        return level(x, root.right, l + 1)
        
def isSibling(root, a, b):
    if root == None:
        return
    if root.left != None and root.right != None:
        if root.left.data == a and root.right.data == b:
            return True
        if root.left.data == b and root.right.data == a:
            return True
    return isSibling(root.left, a, b) or isSibling(root.right, a, b)
    
def isCousin(root, a, b):
    # Your code here

    l1 = level(a, root, 0)
    l2 = level(b, root, 0)
    if l1 == l2 and not isSibling(root, a, b):
        return True
    else:
        return False
    
root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(isCousin(root, 6, 4))

