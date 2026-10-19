from io import StringIO
def count_lines(stream):
    counter = 0
    for line in stream:
        counter += 1
    return counter
print(count_lines(StringIO("first\nsecond\nthird")))
with open('data.txt') as f:
    print(count_lines(f))