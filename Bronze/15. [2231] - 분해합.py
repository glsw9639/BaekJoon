n = int(input())
res = []
for i in range(n):
    lst = list(map(int, str(i)))
    if (n == sum(lst)+ i):
        res.append(i)
        print(*res)
        break
if (res == []):
    print(0)
    