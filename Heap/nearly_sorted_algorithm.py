from heapq import heappush, heappop, heapify
t = int(input())
m = 0
while(m < t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    heap = a[:k]
    heapify(heap)
    ind = k
    for i in range(n - k):
        heappush(heap, a[ind])
        ind += 1
        print(heappop(heap), end = " ")
    while(heap):
        print(heappop(heap), end = " ")
    print()
    m += 1
