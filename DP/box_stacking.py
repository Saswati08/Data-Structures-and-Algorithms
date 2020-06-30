class Box:
    def __init__(self, h, l, w):
        self.height = h
        self.length = l
        self.width = w
def maxHeight(height, width, length, n):
    #Code here
    box_list = []
    for i in range(n):
        b1 = Box(height[i], max(length[i], width[i]), min(length[i], width[i]))
        box_list.append(b1)
        b2 = Box(length[i], max(height[i], width[i]), min(height[i], width[i]))
        box_list.append(b2)
        b3 = Box(width[i], max(length[i], height[i]), min(length[i], height[i]))
        box_list.append(b3)
    
    box_list = sorted(box_list, key = lambda x : x.length * x.width)
    
    dp = [0] * (3 * n)
    for i in range(len(dp)):
        dp[i] = box_list[i].height
    result = dp[0]
    for i in range(1, 3 * n):
        for j in range(i):
            if box_list[i].length > box_list[j].length and box_list[i].width > box_list[j].width and dp[i] < dp[j] + box_list[i].height:
                dp[i] = dp[j] + box_list[i].height
            
            result = max(result, dp[i])
                
    # print(box_list[0].length, box_list[0].width, box_list[0].height)
    return result


