import re
with open('log.txt', 'r', encoding='utf-8') as file:
    infos = 0
    warnings = 0
    errors = 0
    list_of_errors = []
    for user in file:
        if re.findall (r'.+ INFO .+', user):
            infos += 1
        elif re.findall (r'.+ WARNING .+', user):
            warnings += 1
        elif re.match (r'.+ ERROR .+', user):
            a = re.match (r'.+ ERROR User (\d+) .+', user)
            errors+=1
            if a.group(1) not in list_of_errors:
                list_of_errors.append(a.group(1))
print(f"INFO: {infos}")
print(f'WARNING: {warnings}')
print(f'ERROR: {errors}')
for user in list_of_errors:
    print(f"Ошибка встретилась у пользоватля: User {user}")
