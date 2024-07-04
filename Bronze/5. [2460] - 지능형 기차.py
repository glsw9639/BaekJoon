d = []
val = 0
for i in range(10) :
    a,b = map(int, input().split())
    c = b - a
    val += c
    d.append(val)
print(max(d))


