from app.decorators.decorators_cliente import validate_email, validar_cpf
class Cliente:
    def __init__(self, nome, sobrenome, telefone, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = None
        self.cpf_cliente = None

    @validate_email
    def set_email(self, email):
        self.email = email

    @validar_cpf
    def set_cpf(self, cpf_cliente):
        self.cpf_cliente = cpf_cliente
        
    def __str__(self):
        return f"Cliente: {self.nome}, E-mail: {self.email}"
