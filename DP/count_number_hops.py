def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    # code here
    m = 1000000007
    hop_0 = 1
    hop_1 = 1
    hop_2 = 2
    hop_n = 0
    if n == 1:
        return hop_1
    if n == 2:
        return hop_2
    for i in range(n - 2):
        hop_n = (hop_0 + hop_1 + hop_2) % m
        hop_0 = hop_1
        hop_1 = hop_2
        hop_2 = hop_n
        
    return hop_n 

print(countWays(10))
