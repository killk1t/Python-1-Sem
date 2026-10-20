a = str('aaabbbhhccc').lower().replace(' ', '')

m = []
def f(string):
    n = 0
    for char in string:
        if string.count(char)>=n:
            n = string.count(char)
    for char in string:
        if string.count(char)==n:
            m.append(char)
            a = string.replace(char, '')
            n = 0
            
            return a
                
while a!='':
    a = f(a)
    if len(m)==3:
        print(m)
        break

