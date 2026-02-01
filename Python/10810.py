i, j = map(int, input().split(" "))
lst = [0] * i
for _ in range(j):
    a, b, c = map(int, input().split(" "))
    for z in range(a-1, b):
        lst[z] = c

print(*lst)