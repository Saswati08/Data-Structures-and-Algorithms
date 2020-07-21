def isValidIP(s):
    #code here
    arr = s.split(".")
    # print(arr)
    if len(arr) != 4:
        return False
    for i in arr:
        # print(int(i))
        if i.isalpha():
            return False
        if len(i) == 0 or len(i) > 3:
            return False
        if i[0] == '0' and len(i) != 1:
            return False
        if int(i) > 255 or int(i) < 0:
            return False
            
    return True




#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValidIP(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends
