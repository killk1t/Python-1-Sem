#Вариант 3 если что
def f(n, m, first, second):
    if n<0 or m<0: raise ValueError('размеры матрицы обязаны быть положительными')
    d = []
    for row in range(n):
        line = []
        for col in range(m):
            if (row+col)%2==0:
                line.append(first) 
            else:
                line.append(second)
        d.append(line)
    return d

def one_zero_checkerboard(n, m, first=0):
    if first not in (1, 0):
        raise ValueError('Первый элемент обязан быть 0 или 1')
    return f(n, m, first, 1-first)


print(one_zero_checkerboard(3, 5, 0)) 
print(f(1, 3, 'O', 'X'))