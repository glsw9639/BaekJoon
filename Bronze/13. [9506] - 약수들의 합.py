while True:
    a = int(input())
    if a == -1 :
        break
    lst = []
    for i in range(1, a):
        if a % i == 0 :
            lst.append(i)
    if sum(lst) == a :
        print(a, "=", end =' ')
        print(*lst , sep = ' + ')
    else:
        print(a, "is NOT perfect.")
    

