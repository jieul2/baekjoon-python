a, b = map(int, input().split(" "))
answer = 0
for i in range(int(input())):
    c = int(input())

    if c <= 1000:
        answer = c*a
        print(c, answer)
    else:
        answer = a*1000
        print(c, ((c-1000)*b)+answer )
