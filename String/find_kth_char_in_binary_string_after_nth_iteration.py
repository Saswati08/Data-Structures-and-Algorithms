#Given a decimal number m. Convert it in binary string and apply n iterations, in each iteration 0 becomes 01 and 1 becomes 10. Find kth character in the string after nth iteration.
t = int(input())
x = 0
while(x < t):
    m, k, n = map(int, input().strip().split())
    distance = 2 ** n
    block = k // distance
    rem = k % distance
    s = []
    while(m > 0):
        s.append(m % 2)
        m = m // 2
    root = s[len(s) - block - 1]
    # print(root)
    flip = True
    while(rem > 1): 
        if rem & 1 :
            flip = not (flip)
        rem = rem >> 1
    if rem == 0:
        print(root)
    elif flip:
        print(int(not root))
    else:
        print(root)
    x += 1
