t = int(input())
m = 0
while(m < t):
    string = input().strip()
    string_list = list(string.split(" "))
    n = int(input())
    for i in range(len(string_list)):
        print(string_list[i], end = "")
        if i != len(string_list) - 1:
            print("%20", end = "")
    print()
    
    m += 1
