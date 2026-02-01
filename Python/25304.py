total_money = int(input())
money = 0
for _ in range(int(input())):
    a,b = (map(int, input().split()))
    money += (a * b)
    if money > total_money:
        break

if money == total_money:
    print("Yes")
else:
    print("No")