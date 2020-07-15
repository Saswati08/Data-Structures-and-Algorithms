'''
Function Arguments :
		@param  : queue ( given queue to be used), k(Integer ),n(size of queue)
		@return : lsit, just reverse the first k elements of queue and return new queue
'''

def reverseK(queue,k,n):
    # code here
    stack = []
    for i in range(k):
        stack.append(queue.pop(0))
    for i in range(k):
        queue.append(stack.pop(-1))
    for i in range(k, n):
        queue.append(queue.pop(0))
    return queue

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

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
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))

        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*reverseK(queue,k,n))
# } Driver Code Ends
