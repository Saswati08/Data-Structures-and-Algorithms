def reverse(arr, st, f):
    
    while(st < f):
        temp = arr[f]
        arr[f] = arr[st]
        arr[st] = temp
        st += 1
        f -= 1
    # return arr

t = int(input())
m = 0
while(m < t):
    n, d = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    reverse(arr, 0, d - 1)
    # print(arr)
    reverse(arr, d, n - 1)
    # print(arr)
    reverse(arr, 0, n - 1)
    # print(arr)
    for i in arr:
        print(i, end = " ")
    print()
    m += 1
    
