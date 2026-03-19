lst = []
for i in range(int(input())):
    command = input().split()
    if command[0] == "push":
        lst.append(command[1])
    elif command[0] == "pop":
        if len(lst) <= 0:
            print(-1)
            continue
        print(lst[0])
        del lst[0]
    elif command[0] == "size":
        print(len(lst))
    elif command[0] == "empty":
        if len(lst) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(lst) <= 0:
            print(-1)
            continue
        print(lst[0])
    elif command[0] == "back":
        if len(lst) <= 0:
            print(-1)
            continue
        print(lst[-1])