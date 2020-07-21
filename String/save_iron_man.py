# Jarvis is weak in computing palindromes for Alphanumeric characters.
# While Ironman is busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in computing palindromes.
# You are given a string S containing alphanumeric characters. Find out whether the string is a palindrome or not.
# If you are unable to solve it then it may result in the death of Iron Man.
t = int(input())
m = 0
while(m < t):
    alpha_numeric_string = input().strip()
    string = ""
    for i in alpha_numeric_string:
        if i.isalpha():
            if i >= 'A' and i <= 'Z':
                string += chr(ord(i) + 32)
            else:
                string += i
        if i.isdigit():
            string += i
    # print(string)
    flag = 1
    for i in range(len(string)//2):
        if string[i] != string[len(string) - 1 - i]:
            flag = 0
            break
    if flag == 0:
        print("NO")
    else:
        print("YES")
    m += 1
