a = int(input())

if a == 0:
        print("1")
else:

    for i in range(a-1, 0, -1):
          a*= i

    print(a)