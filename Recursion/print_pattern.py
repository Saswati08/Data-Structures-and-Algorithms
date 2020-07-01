#code
# Print a sequence of numbers starting with N, without using loop, in which  A[i+1] = A[i] - 5,  if  A[i]>0, else A[i+1]=A[i] + 5  repeat it until A[i]=N.
def rec(a, n):
    if a > 0:
        print(a , end = " ")
        rec(a - 5, n)
        print(a, end = " ")
    else:
        print(a, end = " ")
        return

t = int(input())
for i in range(t):
    n = int(input())
    rec(n, n)
    print()
        
