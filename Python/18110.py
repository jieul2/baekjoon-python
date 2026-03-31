from decimal import Decimal, ROUND_HALF_UP
diff = []
for _ in range(int(input())):
    diff.append(int(input()))


#정렬
diff.sort() 

#절삭평균 30%  앞뒤 15%씩
s = int(Decimal(len(diff)*(15/100)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
# 앞뒤 15%씩 제거
if s != 0:
  diff = diff[s:-s]
if not diff:
    print(0)
else:
    print(Decimal(sum(diff) / len(diff)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
