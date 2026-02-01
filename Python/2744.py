a = list(input())
b = []

for i in a:
    if 65 <= ord(i) >= 90:
        b.append(i.upper())
    else:
        b.append(i.lower())
print(''.join(b))