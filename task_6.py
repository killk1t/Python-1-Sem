import pathlib
number_of_files = 0
number_of_dirs = 0
list_of_python_files = []
sum_size = 0

#p = pathlib.Path('25')
#print(p.stem, p.suffix)

#p.resolve()
#print(p)

p = pathlib.Path(input('Введите путь к каталогу ')) #('.') . - это спецсимвол, который обозначает текущую рабочую папку (в которой открыт терминал)
if not p.is_dir():
    print(f'Каталог не найден, {p}\n')
    raise SystemExit
for entity in p.rglob('*'):
    if entity.is_dir():
        number_of_dirs += 1
    elif entity.is_file():
        number_of_files += 1
        sum_size += entity.stat().st_size
        if entity.suffix == '.py':
            list_of_python_files.append(entity.relative_to(p))
print(f'Количество файлов: {number_of_files}')
print(f'Количество подкаталогов: {number_of_dirs}')
print('Список всех py файлов:')
for py_file in list_of_python_files:
    print(f' {py_file}')
print(f'Суммарный размер всех файлов: {sum_size} байт')
