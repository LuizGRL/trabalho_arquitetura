from flask import render_template

class ClienteController:
    def cadastrar(self,cliente,db):
        class ClienteBanco(db.Model):
            __tablename__ = 'clientes'
            id = db.Column(db.Integer, primary_key=True,autoincrement = True)
            nome = db.Column(db.String(100), nullable=False)
            sobrenome = db.Column(db.String(100), nullable=False)
            cpf = db.Column(db.String(100), unique=True)
            email = db.Column(db.String(100), unique=True, nullable=False)
            telefone = db.Column(db.String(100))
            data_nascimento = db.Column(db.Date)

        try:
            cliente = cliente
            nome = cliente.nome
            sobrenome = cliente.sobrenome
            email = cliente.email
            telefone = cliente.telefone
            data_nascimento = cliente.data_nascimento
            cpf = cliente.cpf_cliente
            cliente_banco = ClienteBanco(nome=nome, sobrenome=sobrenome,email=email,telefone=telefone,data_nascimento=data_nascimento,cpf=cpf)
            db.session.add(cliente_banco)
            db.session.commit()
            return str(f"Cliente cadastrado com sucesso id: {cliente_banco.id}")
        except Exception as e:
            db.session.rollback()
            return str(f"Erro ao cadastrar o cliente: {str(e)}")

    def renderizar_formulario(self):
        return render_template("cliente_form.html")

cliente_controller = ClienteController()
