for i in range(int(input())):
    row, col, count = map(int, input().split())

# 1 3 1 101호
# 2 3 3 201호
    if count == 1: # 무조건 101호
        print("101")
    elif col == 1 and row != 1: # 무조건 1호
        print(str(count)+"01") 
    elif row == 1 and col != 1: # 무조건 1층
        if count < 10:
            print("1" + "0" + str(count))
        else:
            print("1" + str(count))
    else:
        if row // count == 1 and row % count == 0:
            print(str(count)+"01")
        elif row // count < 0:
            print(str(count)+"01")
        else:
            if count <= row:
                print(str(count) + "01")
            else:
                if count % row == 0:
                    층수 = row
                else:
                    층수 = count % row 
                if count % row == 0:
                    호수 = count // row
                else:
                    호수 = count // row + 1
                if 호수 < 10:
                    호수 = "0" + str(호수)
                
                print(str(층수) + str(호수))