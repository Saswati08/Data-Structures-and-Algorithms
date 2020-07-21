def multiply(a,b):
    # code here
    # return the product string
    sign = 1
    if a[0] == '-':
        sign = -1
        a = a[1:]
    if b[0] == '-':
        sign *= -1
        b = b[1:]
    if len(a) > len(b):
        p1 = a
        p2 = b
    else:
        p1 = b
        p2 = a
    
    j = len(p2) - 1
    s = 0
    ind = 0
    while(j >= 0):
        temp = 0
        s = s + (int(p1) * int(p2[j]) * 10 ** ind)
        j -= 1
        ind += 1
    return s * sign


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(multiply( a.strip() , b.strip() ))

# } Driver Code Ends
