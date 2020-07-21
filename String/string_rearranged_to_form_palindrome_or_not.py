t = int(input())
m = 0
while(m < t):
    string = input().strip()
    hash_map = [0] * 256
    for i in range(len(string)):
        hash_map[ord(string[i])] += 1
    f = 0
    for i in hash_map:
        if i % 2 != 0:
            f += 1
            
    if f == 1 and len(string) % 2 != 0:
        print("Yes")
    elif f == 0 and len(string) % 2 == 0:
        print("Yes")
    else:
        print("No")
    
    m += 1
