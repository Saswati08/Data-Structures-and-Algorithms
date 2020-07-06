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

def isPairPresent(root, target): 
    # code here.
    stack1 = [root]
    stack2 = [root]
    current1 = root
    current2 = root
    while((stack1 or current1) and (stack2 or current2)):
        while(current1):
            stack1.append(current1)
            current1 = current1.left
            
        while(current2):
            stack2.append(current2)
            current2 = current2.right
            
        top1 = stack1[-1]
        top2 = stack2[-1]
        
        if top1.data >= top2.data:
            return 0
        
        if top1.data + top2.data == target:
            # print(top1.data, top2.data)
            return 1
        else:
            if top1.data + top2.data < target:
                stack1.pop(-1)
                current1 = top1.right
                
            if top1.data + top2.data > target:
                stack2.pop(-1)
                current2 = top2.left
                
        
            
    return 0

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)
	print(isPairPresent(root, 25))
    
