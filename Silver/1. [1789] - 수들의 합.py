a = int(input())
i = 0
cnt = 0
while True :
    if (a > i) :
        i += 1
        a -= i
        cnt += 1
    else :
        print(cnt)
        break
    