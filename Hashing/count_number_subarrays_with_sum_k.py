t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    s = int(input())
    hash_map = {}
    curr_sum = 0
    count = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == s:
            count += 1
        if curr_sum - s in hash_map:
            count += hash_map[curr_sum - s]
        if curr_sum not in hash_map:
            hash_map[curr_sum] = 0
        hash_map[curr_sum] += 1
    print(count)
            
    
        
    m += 1
