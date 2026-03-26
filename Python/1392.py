n, q = map(int, input().split())
lst = []

for i in range(n):
    idx = int(input())
    for j in range(idx):
        lst.append(i+1)
for _ in range(q):
    idx_q = int(input())
    print(lst[idx_q])
