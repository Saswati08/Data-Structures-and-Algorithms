'''
	Your task is to check if the given strings are
	isomorphic or not.
	
	Function Arguments: s and p (given strings)
	Return Type: boolean

'''
def areIsomorphic(s,p):
    hash_map1 = {}
    hash_map2 = {}
    if len(s) != len(p):
        return False
    for i in range(len(s)):
        if s[i] not in hash_map1 and p[i] not in hash_map2:
            hash_map1[s[i]] = 1
            hash_map2[p[i]] = 1
        elif s[i] in hash_map1 and p[i] in hash_map2 and hash_map1[s[i]] == hash_map2[p[i]]:
            hash_map1[s[i]] += 1
            hash_map2[p[i]] += 1
        else:
            return False
            
            
    
    return True


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
