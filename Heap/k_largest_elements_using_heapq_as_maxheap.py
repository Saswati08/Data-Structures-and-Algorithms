from heapq import *
t = int(input())
m = 0
while(m < t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    heap = a[:]
    for i in range(n):
        heap[i] = heap[i] * -1
    heapify(heap)
    for i in range(k):
        print(heappop(heap ) * -1, end = " ")
    print()
    m += 1
