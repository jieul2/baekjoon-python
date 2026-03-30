for _ in range(int(input())):
    a, b = map(int,input().split())
    print(b*11+4 if a >= 12 and b >= 4 else -1)