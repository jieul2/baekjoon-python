for _ in range(int(input())):
    num = int(input())
    print("Good" if (num + 1) % int(str(num)[-2:]) == 0 else "Bye")
