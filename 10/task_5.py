def f(a: list, k: int):
    m = []
    if not a:
        return []
    avg = sum(a)/len(a)
    #print(avg)
    c = [(i-avg)**2 for i in a]
    disp = (sum(c)/len(c))**0.5
    for i in a:
        if abs(avg-i)>k*disp:
            m.append(i)
    return m
n = [11, 22, 11, 22, 13, 24]
print(f(n, 1))

#Реализация через numpy
import numpy as np
def f_numpy(a: list, k: int):
    if not a:
        return []
    m = np.array(a)
    mean = m.mean()
    std = m.std()
    mask = (np.abs(m-mean))>k*std
    return m[mask].tolist()
print(f_numpy(n, 1))
print(f_numpy(n, 1) == f(n, 1))