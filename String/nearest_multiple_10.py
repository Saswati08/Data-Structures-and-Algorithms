t = int(input())
m = 0
while(m < t):
    number = list(input().strip())
    last_digit = number[len(number) - 1]
    if int(last_digit) > 5:
        carry = 1
        
    else:
        carry = 0
    number[len(number) - 1] = '0'
    
    i = len(number) - 2
    
    while(i >= 0 and carry > 0):
        k = str((int(number[i]) + carry) % 10)
        carry = (int(number[i]) + carry) // 10
        number[i] = k
        i -= 1
    # print(number, carry)
    if carry == 1:
        number.insert(0, '1')
    
    for i in number:
        print(i, end = "")
    print()
    m += 1
