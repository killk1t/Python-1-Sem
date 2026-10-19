import pathlib
directory = input() # Получаем директорию
exten = input() # Получаем расширение
p = pathlib.Path(directory) # Создаём специальный объект Path, в который передаём директорию для того чтобы применять последующие методы
if not p.exists() or not p.is_dir(): # Проверяем что такая директория существует
    raise NotADirectoryError("Вы ввели некорректную директорию")
else:
    for file in p.rglob(f"*{exten}"): #Рекурентно ищем все файлы в данной директории
        if file.is_file(): # Если найденное является файлом
            print(f'Абсолютный путь до файла: {str(file.absolute())}') # Выводим абсолютный путь найденного файла
            print(f'Размер файла: {file.stat().st_size}') # Выводим размер файла (в байтах)