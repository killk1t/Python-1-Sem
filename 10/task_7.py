def hamming(a:str, b:str):
    count = 0
    if len(a) != len(b):
        return None
    for i in range(len(a)):
        if a[i] != b[i]:
            count+=1
    return count

def close_string_finder(op: list):
    result = []
    minimal_diff = float('inf')
    for i in range(len(op)):
        for j in range(i+1, len(op)):
            difference = hamming(op[i], op[j])
            if difference is not None and difference<minimal_diff:
                minimal_diff = difference
                result = [op[i], op[j]]
    if minimal_diff == float('inf'):
        return None
    return result[0], result[1], minimal_diff


