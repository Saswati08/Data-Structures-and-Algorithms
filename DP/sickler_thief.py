#Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. Each house has a[i] amount of money present in it.
def FindMaxSum(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    # code here
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    if n == 2:
        return max(a[0], a[1])
    dp = []
    dp.append(a[0])
    dp.append(max(a[0], a[1]))
    m = 1000000007
    for i in range(2, n):
        dp.append(max(dp[i - 2] + a[i], dp[i - 1]))
        
    return dp[-1]

FindMaxSum([5, 5, 10, 100, 10, 5], 6)
