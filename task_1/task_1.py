lines = 0
words = 0
chars = 0
maxstr = 0
with open('1.txt') as f:
    for s in f:
        lines +=1
        if len(s)>=maxstr:
            maxstr = len(s)
        a = s.split()
        words += len(a)
        for x in a:
            chars += len(x)
        
print(lines, words, chars, maxstr)