t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    i = 0
    buy = []
    sell = []
    while(i < n):
        while(i < n - 1 and arr[i] > arr[i + 1]):
            i += 1
        if i == n - 1:
            break
        buy.append(i)
        while(i < n - 1 and arr[i] < arr[i + 1]):
            i += 1
        sell.append(i)
        
    for i in range(len(buy)):
        print("(" + str(buy[i]) + " " + str(sell[i]) + ")", end = " ")
    if len(buy) == 0 or len(sell) == 0:
        print("No Profit", end = " ")
    print()
    m += 1
