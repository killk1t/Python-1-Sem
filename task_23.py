import re
text_1 = "Это   строка    с     большим    количеством   пробелов."
text_2 = "   Текст   с   пробелами   "
new_text_1 = re.sub(r'\s+', ' ', text_1)
new_text_2 = re.sub(r'\s+', ' ', text_2)
new_text_2 = re.sub(r'^\s+|\s+$', r'', new_text_2)
print(new_text_1)
print(new_text_2)