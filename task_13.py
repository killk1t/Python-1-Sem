import time 
from contextlib import contextmanager

#Реализация через класс
class Timer:
    def __enter__(self):
        self.starting_time = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):  
        time_elapsed = time.perf_counter() - self.starting_time
        print(f'Время выполнения: {time_elapsed}')
        return False
with Timer():
    time.sleep(0.5)


#Реализация через contextlib.contextmanager
@contextmanager
def timer():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        time_elapsed = time.perf_counter() - start_time
        print(f'Время выполнения: {time_elapsed}')
with timer():
    time.sleep(0.5)

