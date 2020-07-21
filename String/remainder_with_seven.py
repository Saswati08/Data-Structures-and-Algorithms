#Function should return the required answer
#You are not allowed to convert string to integer
def remainderWith7(st):
    #Code here
    div = [1, 3, 2, -1, -3, -2]
    n = 6
    i = len(st) - 1
    pr = 0
    ind = 0
    while(i >= 0):
        pr += int(st[i]) * div[ind]
        ind = (ind + 1) % n
        i -= 1
        
    return pr % 7
    



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        print(remainderWith7(str))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
