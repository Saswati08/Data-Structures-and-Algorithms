#Given an array A of positive integers of size N, where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate packets such that :
#1. Each student gets one packet.
#2. The difference between the number of chocolates given to the students having packet with maximum chocolates and student having packet with minimum chocolates is minimum.
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()] 
    k = int(input())
    a.sort()
    # print(t, n, a, k)
    min_d = a[n - 1]
    for j in range(n - k + 1):
        if a[j + k - 1] - a[j] < min_d:
            min_d = a[j + k - 1] - a[j]
    print(min_d)

