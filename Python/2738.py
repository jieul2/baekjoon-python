a, b = map(int, input().split())

answer_list = [[0] * b for _ in range(a)]
list_a = [list(map(int,input().split())) for _ in range(a)]
list_b = [list(map(int,input().split())) for _ in range(a)]

for i in range(a):
    for j in range(b):
        answer_list[i][j] = list_a[i][j] + list_b[i][j]
        print(answer_list[i][j], end = " ")
    print()


