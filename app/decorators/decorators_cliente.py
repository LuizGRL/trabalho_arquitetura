import re

def validate_email(func):
    def wrapper(self, email):
        if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
            return func(self, email)
        else:
            print("Email inválido!")
    return wrapper

def validar_cpf(func):
    def wrapper(self,cpf_cliente):
        cpf = [int(char) for char in cpf_cliente if char.isdigit()]
        if len(cpf) != 11:
            print("cpf inválido!")
            return None
        if cpf == cpf[::-1]:
            print("cpf inválido!")
            return None
        for i in range(9, 11):
            value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != cpf[i]:
                print("cpf inválido!")
                return None
        return func(self,cpf_cliente)
    return wrapper
