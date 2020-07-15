#Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
#1. The amount of petrol that every petrol pump has.
#2. Distance from that petrol pump to the next petrol pump.
#Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
#Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

'''    lis[][0]:Petrol
    lis[][1]:Distance
'''
#Your task isto complete this function
#Your function should return the starting point
from collections import deque
def tour(lis, n):
    #Code here
    # queue = deque()
    if n == 1:
        if lis[0][0] - lis[0][1] >= 0:
            return 0
        else:
            return -1
    start = 0
    end = 1
    balance = lis[start][0] - lis[start][1]
    while(balance < 0 or start != end):
        
        while(balance < 0 and start != end):
            balance -= lis[start][0] - lis[start][1]
            start = (start + 1) % n
            if start == 0:
                return -1
        balance += lis[end][0] - lis[end][1]
        end = (end + 1) % n
    return start

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends
