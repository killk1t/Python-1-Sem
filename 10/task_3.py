a = 'aaabbbhhccc'


def f(string :str):
    frequency = {}
    for char in string.lower():
        if char != ' ':
            frequency[char] = frequency.get(char, 0) + 1
    remaining = dict(frequency)
    result = []
    while remaining and len(result)<3:
        best_char = max(remaining, key=remaining.get)
        result.append((best_char, remaining.pop(best_char)))
    return result
            

m = f(a) 
print(m)   


