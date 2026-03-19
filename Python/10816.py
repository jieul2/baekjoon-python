input()
list_a = list(map(int, input().split()))
input()
list_b = list(map(int, input().split()))

dic = dict()

for i in list_b:
    dic[i] = 0

for i in list_a:
    if i in (dic.keys()):
        dic[i] += 1
    else:
        pass

print(*dic.values())