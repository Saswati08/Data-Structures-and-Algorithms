def numberOfWays(coins,numberOfCoins,value):
    ways=[0]*(value+1)
    '''
    We declare an array that will contain the number of--
    ways to make change for all values from 0 to value
    This is done as we are working from bottom up. So, obviously, we need to make change for smaller values--
    before we can make change for the given values.
       
    '''
    ways[0]=1#We can make change for 0 in 1 ways, that is by choosing nothing.
    
    for coin in coins:#Using a coin, one at a time
        for i in range(1,value+1):
            if(i>=coin):##Since it makes no sense to create change for value smaller than coin's denomination
                '''
                Write your code here
                We can make change for i by adding number of ways we previously made change for i-coin
                '''
                ways[i] += ways[i - coin]
    return ways[value]

t = int(input())
for m in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    s = int(input())
    arr = [[0 for i in range(s + 1)] for j in range(n + 1)]
    #for i in range(1, n + 1):
        #arr[i][0] = 1
    # print(c)
    #for i in range(1, n + 1):
        #for j in range(1, s + 1):
            
            #if j - c[i - 1] >= 0:
                # print(i, j)
                arr[i][j] = arr[i - 1][j] + arr[i][j - c[i - 1]]
            #else:
                #arr[i][j] = arr[i - 1][j]
    # print(arr)
    #print(arr[n][s])
    print(numberOfWays(c, n, s))

