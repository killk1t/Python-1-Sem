def parse_numer(value: str):
    if value == '': #Проверка и генерация ошибки при пустой строке
        raise ValueError("Передана пустая строка")
    if value.isdigit(): # Проверка что в строке только 
        return float(value)
    else:
        if value.count('-') == 1 and value[0]=='-': # Проверка что в строке один - и он стоит в начале строки
            return parse_numer(value[1:])*(-1)
        if value.count('.') == 1 and ''.join(value.split('.')).isidigit(): # Проверка что одна точка и помимо точки только цифры
            return float(value)
        raise TypeError-("В введённое строке есть запрещённые символы")
n = input()

try:
    print(parse_numer(n))
except TypeError as e:
    print("ошибка типа", e)
except ValueError as e:
    print('Ошибка значения', e)
'''
#9 (Через регулярки)

import re
def parse_number(value: str):
    if re.fullmatch(r"-?\d+(\.\d+)?", value):
        return (float(value))
    raise ValueError ('Строка неверного формата')
'''
'''
import re

s = '2a123'
r = re.fullmatch(r'.?(\w)123', s)
print(r)

s = '123'
print(len(s * -1))
'''