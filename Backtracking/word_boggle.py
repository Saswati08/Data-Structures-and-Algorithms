# Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character.
# Find all possible words that can be formed by a sequence of adjacent characters.
# Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.


#code
import copy
def find_words(boggle, res_words, dictionary, i, j, n, m, words, max_len, words_num, visited):
    if words in dictionary:
        res_words[words] = 1
    if (i == n or j == m or i == -1 or j == -1 or len(words) == max_len):
        return
    if len(res_words) == words_num:
        return
    
    if (i, j) not in visited:
        visited[(i, j)] = 1
        words = words + boggle[i][j]
        # print(words)
        find_words(boggle, res_words, dictionary, i, j + 1, n, m, words, max_len, words_num, visited)
        find_words(boggle, res_words, dictionary, i + 1, j, n, m, words, max_len, words_num, visited)
        find_words(boggle, res_words, dictionary, i - 1, j, n, m, words, max_len, words_num, visited)
        find_words(boggle, res_words, dictionary, i, j - 1, n, m, words, max_len, words_num, visited)
        find_words(boggle, res_words, dictionary, i + 1, j + 1, n, m, words, max_len, words_num, visited)
        find_words(boggle, res_words, dictionary, i + 1, j - 1, n, m, words, max_len, words_num, visited)
        find_words(boggle, res_words, dictionary, i - 1, j + 1, n, m, words, max_len, words_num, visited)
        find_words(boggle, res_words, dictionary, i - 1, j - 1, n, m, words, max_len, words_num, visited)
        visited.pop((i, j))
    
t = int(input())
x = 0
while(x < t):
    words_num = int(input())
    words_list = list(input().split())
    dictionary = dict.fromkeys(words_list, 1)
    max_len = 0
    for i in dictionary:
        if len(i) > max_len:
            max_len = len(i)
    # print(words)
    # print(max_len)
    n, m = map(int, input().split())
    letters = list(input().split())
    boggle = []
    k = 0
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(letters[k])
            k += 1
        boggle.append(temp)
    # print(boggle)
    res_words = {}
    for i in range(0, n):
        for j in range(0, m):
            words = ""
            visited = {}
            find_words(boggle, res_words, dictionary, i, j, n, m, words, max_len, words_num, visited)
    # print(res_words)
    result = list(sorted(res_words.items())) 
    # print(result)
    if len(result) == 0:
        print(-1, end = " ")
    else:
        for i in result:
            print( i[0], end = " ")
    print()
    x += 1
    
    
    
