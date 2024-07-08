a = int(input())
b = int(input())
sosu = []
for i in range(a,b+1):
    if i == 1 :
        continue
    for j in range(2, i):
        if i % j == 0 :
            break
    else :
        sosu.append(i)
if sosu == [] :
    print(-1)
else :
    print(sum(sosu), min(sosu), sep='\n')