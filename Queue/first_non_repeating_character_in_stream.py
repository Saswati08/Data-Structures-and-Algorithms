t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(input().strip().split())
    # print(arr)
    repeated = [0] * 256
    DLL_add = []
    tail = None
    for i in range(len(arr)):
        ch = arr[i]
        if repeated[ord(ch)] == 0:
            if ch in DLL_add:
                DLL_add.remove(ch)
                repeated[ord(ch)] = 1
            else:
                DLL_add.append(ch)
        if DLL_add:
            print(DLL_add[0], end = " ")
        else:
            print("-1", end =  " ")
    print()   
    m += 1
