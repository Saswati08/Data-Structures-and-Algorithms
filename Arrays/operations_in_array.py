# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    # Code here

# fucntion must return true if 
# insertion is successful or else
# return false
    for i in a:
        if i == x:
            return 1
    return 0
def insertEle(a, y, yi):
    # Code here

# fucntion must return true if 
# deletion is successful or else
# return false
    a.insert(yi, y)
    return 1
def deleteEle(a, z):
    # Code here
    if z in a:
        a.remove(z)
        return 1
    else:
        return 1

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        x,y,yi,z = list(map(int, input().strip().split()))
        if(searchEle(a, x)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        if(insertEle(a, y, yi)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        if(deleteEle(a, z)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        print()
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
