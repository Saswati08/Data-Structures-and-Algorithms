class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def calDiagSum(root, sum_map, l):
    if root == None:
        return
    if l not in sum_map:
        sum_map[l] = 0
    sum_map[l] += root.data
    calDiagSum(root.right, sum_map, l)
    calDiagSum(root.left, sum_map, l + 1)
    
def diagonalSum(root):
    #:param root: root of the given tree.
    
    #code here
    sum_map = dict()
    calDiagSum(root, sum_map, 0)
    arr = []
    for keys in sorted(sum_map):
        arr.append(sum_map[keys])
    return arr



root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(diagonalSum(root))
