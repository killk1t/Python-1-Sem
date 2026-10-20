def f(a = list, k = int):
    m = []
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


#Не работал с numpy, поэтому не могу сделать вторую реализацию