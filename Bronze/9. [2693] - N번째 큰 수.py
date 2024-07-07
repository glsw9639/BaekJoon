n = int(input())
while n > 0 :
    lst  = list(map(int, input().split()))
    lst.sort()
    print(lst[7])
    n -= 1