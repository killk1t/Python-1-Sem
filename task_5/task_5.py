import json
students = 'students.json'
max_score = 0
best_student = None
with open(students) as f:
    students_data = json.load(f)
#   json.load() используется для чтения из файла <json>
#   json.loads() используется для чтения строки, у которой синтаксис как у json файла (можно получить с помощью f = read('file.json'))
#   print(students_data)
    for i in students_data:
        i["passed"] = i['score']>80 #True or False
        if i['score']>max_score:
            max_score = i['score']
            best_student = i['name']
#   print(students_data)
    with open('new_students.json', 'w') as file:
        json.dump(students_data, file, indent=1)
print(best_student)