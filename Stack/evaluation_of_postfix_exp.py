t = int(input())
m = 0
while(m < t):
    postfix = input()
    stack = []
    stack.append(postfix[0])
    stack.append(postfix[1])
    i = 2
    while(i < len(postfix)):
        ip = postfix[i]
        if ip != '*' and ip != '/' and ip != '+' and ip != '-':
           stack.append(ip)
        else:
            
            op2 = int(stack.pop(-1))
            op1 = int(stack.pop(-1))
            if ip == '*':
                res = op1 * op2
            elif ip == '/':
                res = op1//op2
            elif ip == '+' :
                res = op1 + op2
            elif ip == '-':
                res = op1 - op2
            # print(res)
            stack.append(res)
        i += 1
    print(stack.pop())
    m += 1
