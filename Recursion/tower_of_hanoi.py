def tower_of_hanoi(n, s, intr, d, c):
    if n == 1:
        print("move disk "+ str(1)+ " from rod " + str(s)+ " to rod " + str(d))
        return 1
    c1 = tower_of_hanoi(n - 1, s, d, intr, 0)
    print("move disk "+ str(n)+" from rod " + str(s)+" to rod " + str(d))
    c2 = tower_of_hanoi(n - 1, intr, s, d, 0)
    return c1 + c2 + 1
        
    
    
t = int(input())
m = 0
while(m < t):
    n = int(input())
    if n == 2:
        print("move disk 1 from rod 1 to rod 2")
        print("move disk 2 from rod 1 to rod 3")
        print("move disk 1 from rod 2 to rod 3")
        print("3")
    else:
        c = tower_of_hanoi(n, 1, 2, 3, 0)
        print(c)
    m += 1
