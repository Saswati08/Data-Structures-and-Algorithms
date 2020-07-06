class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
def construct_tree(inorder_arr, index):
    if index[0] > index[1]:
        return None
    mid = (index[0] + index[1])//2
    key = inorder_arr[mid]
    nw = Node(key)
    nw.left = construct_tree(inorder_arr, [index[0], mid - 1])
    nw.right = construct_tree(inorder_arr, [mid + 1, index[1]])
    return nw

def preorder_traversal(root):
    if root == None:
        return
    print(root.data, end = " ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    root = construct_tree(arr, [0, len(arr) - 1])
    preorder_traversal(root)
    print()
    m += 1
