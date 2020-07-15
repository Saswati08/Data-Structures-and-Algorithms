def find_celebrity(m, n):
    if n == 1:
        return 0
    id_n_1 = find_celebrity(m, n - 1)
    if id_n_1 == -1:
        return n - 1
    else:
        if m[id_n_1][n - 1] == 0 and m[n - 1][id_n_1] == 1:
            return id_n_1
        if m[n - 1][id_n_1] == 0 and m[id_n_1][n - 1] == 1:
            return n - 1
        return -1
def getId(m,n):
    # code here
    prob_celeb = find_celebrity(m, n)
    c1 = 0
    c2 = 0
    for i in range(n):
        if i != prob_celeb:
            c1 += m[i][prob_celeb]
            c2 += m[prob_celeb][i]
            
    if c1 == n - 1 and c2 == 0:
        return prob_celeb
    else:
        
        return -1
        

m = [[0, 1, 0 ],[0, 0, 0],[0, 1, 0]]
print(getId(m, n))
