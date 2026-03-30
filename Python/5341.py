while True:
    a = int(input())
    sum = 0
    if a == 0:
        break
    for i in range(1, a+1):
        sum += i
    print(sum)