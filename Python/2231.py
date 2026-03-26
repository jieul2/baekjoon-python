idx = int(input())
count_idx = idx+1
max_idx = idx
answer_idx = 0
answer_lst = []


while True:
    count_idx -= 1
    lst = [int(a) for a in str(count_idx)]
    answer_idx = count_idx + sum(lst) 
    
    if  answer_idx == idx:
        if max_idx > answer_idx:
            max_idx = count_idx
        answer_lst.append(count_idx)
    if count_idx == (idx//2) or count_idx < 0:
        break
    
if(len(answer_lst) == 0):
    print(0)
else:
    print(min(answer_lst))
        
        
