def ispar(s):
    # code here
    if len(s) == 0:
        return True
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        
        if s[i] == '[' or s[i] == '(' or s[i] == '{':
            stack.append(s[i])
        elif len(stack) == 0:
            return False
        else:
            top = stack.pop(-1)
            if s[i] == ']' and top != '[':
                return False
            elif s[i] == '}' and top != '{':
                return False
            elif s[i] == '(' and top != ')':
                return False
                
            
            
    if len(stack) != 0:
        return False
        
    return True
            

print(ispar("{}[]()"))
