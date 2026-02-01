#input()
lst = map(int,input().split())
count = 0

for i in lst:
    count1 = 0
    if i == 1:
        continue
    if i == 2 or i == 3 or i == 5 or i == 7 or i == 13:
        count += 1
        continue
    for j in range(2, i // 2+1):
        if i % j == 0:
            count1 += 1
            break
    if count1 == 0:
        count += 1
        
            

print(count)