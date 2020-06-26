

def printPostOrder(inorder, preorder, n):
    # Code here
    ind = inorder.index(preorder[0])
    
    if ind != 0:
        printPostOrder(inorder[:ind], preorder[1: ind + 1], len(inorder[:ind]))
    if ind != n - 1:
        printPostOrder(inorder[ind + 1:], preorder[ind + 1:], len(inorder[ind + 1:]))
        
    print(preorder[0], end = " ")


inorder = [4, 2, 5, 1, 3, 6] 
preorder = [1, 2, 4, 5, 3, 6]
n = len(inorder) 
printPostOrder(inorder, preorder, n)
