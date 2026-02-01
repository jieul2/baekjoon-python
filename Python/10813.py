a, b = map(int, input().split())

lst = [i for i in range(1, a+1)]

for _ in range(b):
    c, d = map(int, input().split())
    lst[c-1], lst[d-1] = lst[d-1], lst[c-1]


print(*lst)