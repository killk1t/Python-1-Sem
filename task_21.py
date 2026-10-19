import re
def is_valid_login(login: str):
    if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]{3,15}', login): #не уверен, стоит ли допускать заглавные латинские буквы
        return True
    return False
print(is_valid_login(''))