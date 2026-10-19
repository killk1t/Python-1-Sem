import re
products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]
correct = []
for product in products:
    if re.fullmatch(r'PRD-\d{5}', product):
        correct.append(product)
print(correct)