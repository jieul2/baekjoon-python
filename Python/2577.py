dic = {
    0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 
}

a = int(input())
b = int(input())
c = int(input())

for i in list(str(a*b*c)):
    dic[int(i)] += 1



for j in range(10):
    print(dic[j])