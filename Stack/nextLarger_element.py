def nextLargerElement(arr,n):
    #code here
    stack = []
    nextLarger = [0] * n
    i = n - 1
    while(i >= 0):
        if not stack:
            stack.append(i)
            nextLarger[i] = -1
        else:
            while(stack and arr[stack[-1]] <= arr[i]):
                stack.pop(-1)
            
            if stack:
                nextLarger[i] = arr[stack[-1]]
            else:
                nextLarger[i] = -1
            stack.append(i)
        i -= 1
    return nextLarger
    

print(nextLargerElement[1, 3, 2, 4], 4)
