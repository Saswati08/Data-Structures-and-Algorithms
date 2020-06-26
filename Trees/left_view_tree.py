def printLeftView(root, visited, level):
    if root == None:
        return 
    if visited[level] == 0:
        print(root.data, end = " ")
        visited[level] = 1
    printLeftView(root.left, visited, level + 1)
    printLeftView(root.right, visited, level + 1)
def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    visited = [0] * 100
    printLeftView(root, visited, 0)
    # print()

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(LeftView(root))
