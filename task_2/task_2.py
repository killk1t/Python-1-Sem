import math
min = float('inf')
max = float('-inf')
sum = 0
k = 0
with open('integers_50_lines.txt') as f:
    for s in f:
        
        try:
            int(s)
        except Exception:
            continue
        else:
            k+=1
            if int(s)<min:
                min = int(s)
            if int(s)>max:
                max = int(s)
            sum+=int(s)



with open('result.txt', 'w', encoding= 'utf-8') as file:
    file.write(f'{min}\n')
    file.write(f'{max}\n')
    file.write(f'{sum/k}\n')