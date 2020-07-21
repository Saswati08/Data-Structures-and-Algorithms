def find_candidate(a):
    max_index = 0
    count = 1
    for i in range(1, len(a)):
        if a[i] == a[max_index]:
            count += 1
        elif count > 0:
            count -= 1
        
        if count == 0:
            max_index = i
            count = 1
            
    return a[max_index]
    
def majority_element(cand, arr):
    c = 0
    for i in arr:
        if i == cand:
            c += 1
    if c > len(arr)//2:
        return 1
    else:
        return 0
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    cand = find_candidate(arr)
    # print(cand)
    f = majority_element(cand, arr)
    if f == 1:
        print(cand)
    else:
        print(-1)
    m += 1
