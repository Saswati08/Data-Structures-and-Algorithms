def handshakes(n):
    if n == 0:
        return 1
    if n in hash_map:
        return hash_map[n]
    else:
        c = 0
        for i in range(0, n, 2):
            c += handshakes(i) * handshakes(n - 2 - i)
        hash_map[n] = c
        return c
        

t = int(input())
hash_map = {}
handshakes(30)

m = 0
while(m < t):
    n = int(input())
    # print(hash_map[8])
    print(hash_map[n])
    
    m += 1

