lst = []
count = int(input())
for _ in range(count):
    a, b = map(int, input().split())

    if str(a)[-1:] == "1":
        lst.append(1)

    elif str(a)[-1:] == "2":
        num = [ 6, 2, 4, 8 ]
        lst.append(num[b%4])
    

    elif str(a)[-1:] == "3":
        num = [ 1, 3, 9, 7 ]
        lst.append(num[b%4])

    elif str(a)[-1:] == "4":
        num = [ 6, 4 ]
        lst.append(num[b%2])

    elif str(a)[-1:] == "5":
        lst.append(5)
        

    elif str(a)[-1:] == "6":
        lst.append(6)
        

    elif str(a)[-1:] == "7":
        num = [ 1, 7, 9, 3 ]
        lst.append(num[b%4])

    elif str(a)[-1:] == "8":
        num = [ 6, 8, 4, 2 ]
        lst.append(num[b%4])

    elif str(a)[-1:] == "9":
        num = [ 1, 9 ]
        lst.append(num[b%2])

    else:
        lst.append(10)

for i in lst:
    print(i)