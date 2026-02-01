lst = []
n = int(input())
count = 0
for i in range(n):
    lst.append(int(input()))


print(sum(lst) - n+1)