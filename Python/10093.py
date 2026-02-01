a, b = map(int, input().split())

if a > b:
    lst = [i for i in range(b+1, a)]
else : 
    lst = [i for i in range(a+1, b)]

print(len(lst))
lst.sort()
print(" ".join(map(str, lst)))