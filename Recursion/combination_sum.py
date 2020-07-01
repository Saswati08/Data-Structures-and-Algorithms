#User function Template for python3
# Given an array of integers and a sum B, find all unique combinations in the array where the sum is equal to B. The same number may be chosen from the array any number of times to make B.
import copy
def combination(s, A, res, ind, comb):
    if s == 0:
       res.append(comb)
    #   return res
     
    elif s < 0:
         return res
    i = ind
    while(i < len(A) and s - A[i] >= 0):
        #  print(comb)
         cpy = copy.deepcopy(comb)
         cpy.append(A[i])
        #  res = combination(s - A[i], A, res, i, comb)
         combination(s - A[i], A, res, i, cpy)
         i += 1
        #  comb = comb[:len(comb) - 1]
    # return res

def combinationalSum(A, B):
    '''
    :param A: given array A
    :param B: given sum to be achieved
    :return: list containing list of numbers in ascending order, giving the combinational sum
    '''
    # code here
    A = set(A)
    A = list(A)
    A = sorted(A)
    # print(A)
    res = []
    combination(B, A, res, 0, [])
    # print(res)
    return res

combinationalSum([1, 1, 2, 3], 6 0)
