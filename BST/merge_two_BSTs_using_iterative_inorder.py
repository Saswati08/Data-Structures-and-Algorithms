class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
def insert(root, key):

	# if the root is None, create a node and return it
	if root is None:
		return Node(key)

	# if given key is less than the root node, recur for left subtree
	if key < root.data:
		root.left = insert(root.left, key)

	# if given key is more than the root node, recur for right subtree
	else:
		root.right = insert(root.right, key)

	return root

def merge(root1, root2):
    #code here.
    if root1 == None or root2 == None:
        return []
    stack1 = [root1]
    stack2 = [root2]
    current1 = root1.left
    current2 = root2.left
    
    res = []
    while((stack1 or current1) and (stack2 or current2)):
        
        
        while(current1):
            stack1.append(current1)
            current1 = current1.left
            
        while(current2):
            stack2.append(current2)
            current2 = current2.left
            
        top1 = stack1[-1]
        top2 = stack2[-1]
        if top1.data == top2.data:
            res.append(top1.data)
            res.append(top2.data)
            stack1.pop(-1)
            current1 = top1.right
            stack2.pop(-1)
            current2 = top2.right
            
        elif top1.data < top2.data:
            res.append(top1.data)
            stack1.pop(-1)
            current1 = top1.right
            
        elif top2.data < top1.data:
            res.append(top2.data)
            stack2.pop(-1)
            current2 = top2.right
            
    while(True):
        while(current1):
            stack1.append(current1)
            current1 = current1.left
            
        if stack1:
            top1 = stack1[-1]
            stack1.pop(-1)
            res.append(top1.data)
            current1 = top1.right
        
        else:
            break
                
    while(True):
        while(current2 != None):
            # print("here")
            stack2.append(current2)
            current2 = current2.left
            
        # print(stack2, stack2[-1].data)
        # break
            
        if len(stack2) > 0:
            top2 = stack2[-1]
            stack2.pop()
            res.append(top2.data)
            current2 = top2.right   
        # print(current2, stack2)    
        # break
        else:
            break

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)
	keys2 = [1, 2, 3, 4, 5]
	for key in keys2:
		root2 = insert(root2, key)
	

	print(merge(root, root2))
	

