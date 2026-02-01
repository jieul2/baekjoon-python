count = int(input())
shirt = [int(i) for i in input().split()]
a, b = map(int, input().split())
shirt_count = 0
for i in shirt:
    if i == 0:
        pass
    elif i % a == 0:
        shirt_count += i // a
    else:
        shirt_count += i // a + 1

print(shirt_count)
print(f"{count // b} {count % b}")