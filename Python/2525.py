a, b = map(int, input().split())
c = int(input())

time = (a*60) + b + c
a = time%60
time = time//60
if time >= 24:
    time -= 24
print(f"{time} {a}")
