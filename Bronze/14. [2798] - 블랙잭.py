a, b = map(int, input().split())
lst = list(map(int , input().split()))
sum = 0
res = []
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            sum = lst[i] + lst[j] + lst[k]
            if sum <= b :
                res.append(sum)
print(max(res))

            