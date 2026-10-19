import csv
students_count = 0
students_sum = 0
max_score = 0
best_student = None
group_score = dict()
with open('students.csv') as file:
    reader = csv.reader(file)
    headers = next(reader) #reader - это итератор
    for row in reader:
        print(row)
        students_count +=1
        students_sum += int(row[2])
        if int(row[2])>max_score:
            max_score = int(row[2])
            best_student = row[0]
        if int(row[1] not in group_score):
            group_score[int(row[1])] = [1, int(row[2])]
        else:
            group_score[int(row[1])][0] += 1
            group_score[int(row[1])][1] += int(row[2])
print(best_student)
print(students_sum/students_count)
for group_number in group_score:
    avg = group_score[group_number][1]/group_score[group_number][0]
    print(f'Группа {group_number}:', avg)