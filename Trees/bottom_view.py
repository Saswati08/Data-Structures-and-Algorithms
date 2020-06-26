class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def stBottomView(root, map_, l):
    if root == None:
        return
    # if l not in map_:
    map_[l] = (root.data)
    # elif d >= map_[l][1]:
    #     map_[l] = (root.data, d)
    stBottomView(root.left, map_, l - 1)
    stBottomView(root.right, map_, l + 1)
    
def bottomView(root):
    '''
    :param root: root of the binary tree
    :return: list containing the bottom view from left to right
    '''
    # code here
    map_ = dict()
    stBottomView(root, map_, 0)
    arr = []
    for keys in sorted(map_):
        arr.append(map_[keys])
        # print(keys)
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
print(bottomView(root))
