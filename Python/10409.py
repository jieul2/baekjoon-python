n, t = map(int, input().split())
lst = list(map(int, input().split()))
idx = 0
while True:
    if idx >= n or t == 0 or t < lst[idx]:
        print(idx)
        break
    t -= lst[idx]
    idx += 1

