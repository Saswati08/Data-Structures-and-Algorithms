t = int(input())
m = 0
while(m < t):
    string = input().strip()
    pattern = input().strip()
    start = 0
    hash_map_p = {}
    hash_map_s = {}
    count = 0
    minm = float('inf')
    mini = -1
    for i in range(len(pattern)):
        if pattern[i] not in hash_map_p:
            hash_map_p[pattern[i]] = 0
        hash_map_p[pattern[i]] += 1
    for i in range(len(string)):
        if string[i] not in hash_map_s:
            hash_map_s[string[i]] = 0
        hash_map_s[string[i]] += 1
        if string[i] in hash_map_p and hash_map_s[string[i]] <= hash_map_p[string[i]]:
            count += 1
        if(count == len(pattern)):
            # print(i, string[i])
            while(string[start] not in hash_map_p or hash_map_s[string[start]] > hash_map_p[string[start]]):
                if string[start] in hash_map_p and hash_map_s[string[start]] > hash_map_p[string[start]]:
                    hash_map_s[string[start]] -= 1
                start += 1
            
            w = i - start + 1
            if w < minm:
                minm = w
                mini = start
                # print(string[start:start + w])
    if mini == -1:
        print(-1)
    else:
        print(string[mini: mini + minm])
            
            
    m += 1
