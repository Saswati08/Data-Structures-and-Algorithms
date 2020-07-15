def max_of_subarrays(arr,n,k):
    '''
    you can use collections module here.
    :param a: given array
    :param n: size of array
    :param k: value of k
    :return: A list of required values 
    '''
    #code here
    queue = deque()
    for i in range(k):
        while(queue and arr[i] >= arr[queue[-1]]):
            queue.pop()
            
        queue.append(i)
    i = k
    res = []
    while(i < n):
        front = queue[0]
        res.append(arr[front])
        while(queue and queue[0] <= i - k):
            queue.popleft()
        while(queue and arr[queue[-1]] <= arr[i]):
            queue.pop()
        queue.append(i)
        i += 1
    res.append(arr[queue[0]])
    return res    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

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
        arr = list(map(int,input().strip().split()))
        res = max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
