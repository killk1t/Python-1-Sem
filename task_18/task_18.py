import re
import logging
import json

error_count = 0

most_frequent_url = None
log_counter = {}
url_counter = {}


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', filename='process.log', filemode='a')
logger = logging.getLogger(__name__)
def read_file(file):
    logs = []
    logger.info('Чтение файла %s', file)
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                m = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<HTTP_method>[A-Z]+) (?P<URL>\S+) (?P<Answer_code>\d{3})', line)
                if m:
                    m = m.groupdict()
                    logs.append(m) #Извлёк IP, HTTP-метод, URL и код ответа;
                else:
                    logger.warning('Пропустил строку %s', line.rstrip())
    except FileNotFoundError:
        logger.error('Файл не найден %s', file)
    except PermissionError:
        logger.error('Недостаточно прав %s', file)
    except IsADirectoryError:
        logger.error('%s папка, а не файл', file)
    except UnicodeDecodeError:
        logger.error('Файл %s не в нужной кодировке', file)
    except OSError:
        logger.error('Возникла другая ошибка ОС при чтении %s', file)
    else:
        logger.info('Прочитано строк: %d', len(logs))
        return logs
    finally:
        logger.info('Работа с файлом %s завершена', file)
    return 1

all_logs = read_file('access.log')
if all_logs != 1:
    for log in all_logs:
        method = log["HTTP_method"]
        if method not in log_counter:
            log_counter[method] = 0
        log_counter[method] += 1
        error = log["Answer_code"]
        if re.match(r'4\d{2}', error):
            error_count+=1
        url = log["URL"]
        if url not in url_counter:
            url_counter[url] = 0
        url_counter[url] += 1

    max_url_count = max(url_counter.values(), default=0)
    for key, value in url_counter.items():
        if value == max_url_count:
            most_frequent_url = key
    stats = {
    'requests_by_method': log_counter,
    'errors_4xx': error_count, 
    'most_frequent_url': most_frequent_url,
    'most_frequent_url_count': max_url_count
    }
    with open('stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=3)
        logger.info('Все данные сохранены в JSON файле %s', 'stats.json')
else:
    logger.error('Дальнейшее выполнение программы невозможно, так как не удалось прочитать файл')
#        print(key)
#print(log_counter)
#print(all_logs)