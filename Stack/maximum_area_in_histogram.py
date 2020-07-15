def getMaxArea(histogram):
    #code here
    i = 0
    stack = []
    max_area = float('-inf')
    while(i < len(histogram)):
        if not stack or histogram[stack[-1]] <= histogram[i]:
            stack.append(i)
            i += 1
        else:
            while(stack and histogram[stack[-1]] > histogram[i]):
                top = histogram[stack.pop(-1)]
                if stack:
                    area = top * (i - stack[-1] - 1)
                else:
                    area = top * i
                max_area = max(max_area, area)
                
    while(stack):
        top = histogram[stack.pop(-1)]
        if stack:
            area = top * (i - stack[-1] - 1)
        else:
            area = top * i
        max_area = max(max_area, area)
        
    return max_area
        

print(getMaxArea([7, 4, 9, 5, 2]))
