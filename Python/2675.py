
for i in range(int(input())):
    answer = ''
    a, b = input().split(" ")

    for i in list(b):
        answer += i*int(a)

    print(answer)