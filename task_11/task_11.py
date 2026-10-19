import re
with open('log.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    ids = re.findall(r'User (\d+)', text)
    error_lines = re.findall(r'^ERROR.*', text, flags=re.MULTILINE)
    error_ids = re.findall(r'^ERROR User (\d+).*', text, flags=re.MULTILINE)
print(f'Идентификаторы пользователей: {ids}')
for line in error_lines:
    print(f'Строка с ERROR: {line}')
print(f'Идентификаторы пользователей с ошибкой: {error_ids}')