def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файла с таким адресом не существует\n {path}")
    except PermissionError:
        print(f"Ошибка прав доступа: {PermissionError.__name__, path}")
    except IsADirectoryError:
        print(f'Введённый файл является папкой: {IsADirectoryError.__name__}, path = {path}') # Не уверен, что подразумевалось под "невозможностью прочиать файл", возможно здесь должна стоять другая ошибка
    except UnicodeDecodeError:
        print(f"Не удалось прочитать файл из-за ошибки кодировки: {UnicodeDecodeError.__name__, path}")
    except OSError as e:
        print(f'Возникла ошибка операционной системы: {e.__class__.__name__, e}')
    except Exception as e:
        print(f"Ошибка класса {e.__class__.__name__}")
    return None
content = read_file(input())
if content is not None:
    print(content)