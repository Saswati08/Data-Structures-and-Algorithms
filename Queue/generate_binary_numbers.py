'''
Function Arguments :
		@param  : n (given number)
		@return : list of all the binary numbers till n.
'''
def GenerateBinary(n):
    # code here
    queue = ['1']
    res = ['1']
    while(len(res) < n):
        front = queue.pop(0)
        queue.append(front + '0')
        res.append(front + '0')
        if len(res) == n:
            return res
        queue.append(front + '1')
        res.append(front + '1')
    return res
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by :  Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = GenerateBinary(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
# } Driver Code Ends
