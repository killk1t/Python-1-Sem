a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(a[0][0])

def f(op):
    c = 0
    d = 0
    b = []
    
    g = []
    for i in op:
        c = len(op)
        for n in i:
           d = len(i)  
           b.append(n)
#   print(c, d)
    e = []
    m = 0
    for m in range(m, m+d):
        for n in range(c-1, -1, -1):
            e.append(b[m+d*n])
        g.append(e)
        e = []
        
    return g


print(f(a))
