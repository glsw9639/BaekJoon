a = int(input())
while a > 0:
    b = bin(int(input()))[2:]
    string = list(reversed(b)) 
    for i in range(len(string)):
        if string[i] == '1':
            print(i, end=" ")
    a -= 1
