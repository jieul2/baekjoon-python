dic = {"D":0, "P":0}

for _ in range(int(input())):
    a = input()
    if dic['D'] - dic['P'] == 2 or dic['P'] - dic['D'] == 2:
        pass
    else:
        dic[a] += 1

print(f"{dic['D']}:{dic['P']}")