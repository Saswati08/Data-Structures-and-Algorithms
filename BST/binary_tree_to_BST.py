class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def change_tree(arr, root, index):
    if index[0] >= len(arr) or root == None:
        return
    change_tree(arr, root.left, index)
    root.data = arr[index[0]]
    index[0] += 1
    change_tree(arr, root.right, index)
def preorder_traversal(root):
    if root == None:
        return
    print(root.data, end = " ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

    
def conv_tree_arr(root, arr):
    if root == None:
        return
    
    conv_tree_arr(root.left, arr)
    arr.append(root.data)
    conv_tree_arr(root.right, arr)
def binaryTreeToBST(root):
    # code here
    arr = []
    conv_tree_arr(root, arr)
    arr = sorted(arr)
    # print(arr)
    change_tree(arr, root, [0])

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(3)

binaryTreeToBST(root)
preorder_traversal(root)

