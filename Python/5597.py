alist = [i for i in range(1, 31)]
blist = []
for i in range(28):
    blist.append(int(input()))
c = sorted(list(set(alist) - set(blist)))

for i in c:
    print(i)