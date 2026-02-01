lst = []
diff_idx = set()
count = int(input())
for _ in range(count):
    lst.append(list(input()))



for i in range(count - 1 ):
    for j in range(len(lst[0])):
        if lst[i][j] != lst[i+1][j]:
            diff_idx.add(j)
a = lst[0]
for z in diff_idx:
    a[z] = "?"

print("".join(a))