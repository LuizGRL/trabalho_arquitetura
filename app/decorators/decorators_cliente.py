import re

def validate_email(func):
    def wrapper(self, email):
        if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
            return func(self, email)
        else:
            print("Email inválido!")
    return wrapper
