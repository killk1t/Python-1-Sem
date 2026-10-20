import random
from functools import wraps


def retry(times):
    if times < 1:
        raise ValueError('Число попыток должно быть не меньше 1')

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    print(f'{func.__name__}: попытка {attempt} из {times} не удалась: {error!r}')
                    if attempt == times:
                        raise
        return wrapper
    return decorator


@retry(3)
def load_data():
    if random.random() < 0.5:
        raise ConnectionError('Сеть недоступна')
    return 'данные загружены'

print(load_data())

