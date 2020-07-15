def greater(ch, top):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
    if top in precedence:
        return precedence[top] >= precedence[ch]
    else:
        return False
def InfixtoPostfix(exp):
    #code here
    postfix = ""
    stack = []
    
    for i in range(len(exp)):
        ch = exp[i]
        # print(ch)
        if ch.isalpha():
            postfix += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while(stack and stack[-1] != '('):
                postfix += stack.pop(-1)
                
            if len(stack) != 0:
                
                stack.pop(-1)
                
        else:
            # print(ch)
            # print(stack)
            while(stack and greater(ch, stack[-1])):
                postfix += stack.pop(-1)
            stack.append(ch)
    while(stack):
        postfix += stack.pop(-1)
    return postfix
            
    
print(InfixtoPostfix("abcd^e-fgh*+^*+i-"))
