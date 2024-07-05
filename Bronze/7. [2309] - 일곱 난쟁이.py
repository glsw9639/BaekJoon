a = []
temp1, temp2 = 0, 0
for i in range(9):
    b = int(input())
    a.append(b)
a.sort()
val = sum(a) - 100
for i in range(9):
    for j in range(i+1, 9):
        if (a[i] + a[j] == val) :
            temp1 = a[i]
            temp2 = a[j]
a.remove(temp1)
a.remove(temp2)
print("\n".join(map(str, a)))
        

