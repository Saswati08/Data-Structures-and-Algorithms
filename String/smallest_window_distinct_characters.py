t = int(input())
m = 0
while(m < t):
    string = input().strip()
    hash_map_d = {}
    for i in range(len(string)):
        if string[i] not in hash_map_d:
            hash_map_d[string[i]] = 1
    hash_map_s = {}
    count = 0
    start = 0
    mini = -1
    minm = float('inf')
    for i in range(len(string)):
        if string[i] not in hash_map_s:
            hash_map_s[string[i]] = 0
        hash_map_s[string[i]] += 1
        if hash_map_s[string[i]] == 1:
            count += 1
        if count == len(hash_map_d):
            while(hash_map_s[string[start]] > 1):
                hash_map_s[string[start]] -= 1
                start += 1
            w = i - start + 1
            if w < minm :
                minm = w
                mini = start
    print(minm)
    m += 1
