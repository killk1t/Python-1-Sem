a = [1, 1, 1, 2, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1]
def f(x):
    k = 1
    m = 0
    n = 0
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            k+=1
            if k>m:
                m=k
                n = x[i]
        else:
            k = 1
    print(m)
    print(n)
f(a)
