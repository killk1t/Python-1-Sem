import math
min_number = float('inf')
max_number = float('-inf')
count = 0
total = 0
with open('numbers.txt', 'r', encoding='utf-8') as f:
    for number in f:
        number = int(number)
        count += 1
        total += number
        if number<min_number:
            min_number = number
        if number>max_number:
            max_number = number
print(total)
print(min_number)
print(max_number)
print(count)
print(total/count)