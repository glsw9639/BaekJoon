import sys

a = int(input())
b = int(input())
c = a * (b % 10)
d = a * ((b // 10) % 10)
e = a * (b // 100)
f = c + (d * 10) + (e * 100)

print(c, d, e, f, sep = "\n")