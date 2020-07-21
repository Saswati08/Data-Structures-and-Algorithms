# function should return an integer
def atoi(string):
    # Code here
    sign = 1
    if string[0] == '-':
        string = string[1:]
        sign *= -1
    s = 0
    value = {'0' : 0, '1': 1, '2': 2, '3': 3, '4' : 4, '5': 5, '6': 6, '7' : 7, '8': 8, '9' : 9}
    for i in range(len(string)):
        if string[i] > '9' or string[i] < '0':
            return -1
        s = s * 10 + value[string[i]] 
    return s * sign



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        print(atoi(string))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends
