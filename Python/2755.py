from decimal import Decimal

dic = {
    "A+" : Decimal("4.3"), "A0" : Decimal("4.0"), "A-" : Decimal("3.7"),
    "B+" : Decimal("3.3"), "B0" : Decimal("3.0"), "B-" : Decimal("2.7"),
    "C+" : Decimal("2.3"), "C0" : Decimal("2.0"), "C-" : Decimal("1.7"),
    "D+" : Decimal("1.3"), "D0" : Decimal("1.0"), "D-" : Decimal("0.7"),
    "F" : Decimal("0.0")
}

a = int(input())
total = Decimal("0")
hakjum = Decimal("0")

for _ in range(a):
    name, credit, grade = input().split()
    credit = Decimal(credit)
    hakjum += credit
    total += credit * dic[grade]

avg = total / hakjum
print(f"{avg:.2f}")
