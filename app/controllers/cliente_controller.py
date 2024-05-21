from flask import render_template


class ClienteController:
    def cadastrar(self,cliente,db):
        class ClienteBanco(db.Model):
            __tablename__ = 'clientes'
            __table_args__ = {'extend_existing': True}
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
        
        
    def listar_cliente(self,db):
        class ClienteBanco(db.Model):
            __tablename__ = 'clientes'
            __table_args__ = {'extend_existing': True}
            id = db.Column(db.Integer, primary_key=True,autoincrement = True)
            nome = db.Column(db.String(100), nullable=False)
            sobrenome = db.Column(db.String(100), nullable=False)
            cpf = db.Column(db.String(100), unique=True)
            email = db.Column(db.String(100), unique=True, nullable=False)
            telefone = db.Column(db.String(100))
            data_nascimento = db.Column(db.Date)
        clientes = ClienteBanco.query.all()
        return clientes
            
    def obter_cliente_por_id(self,db,id):
        class ClienteBanco(db.Model):
            __tablename__ = 'clientes'
            __table_args__ = {'extend_existing': True}
            id = db.Column(db.Integer, primary_key=True,autoincrement = True)
            nome = db.Column(db.String(100), nullable=False)
            sobrenome = db.Column(db.String(100), nullable=False)
            cpf = db.Column(db.String(100), unique=True)
            email = db.Column(db.String(100), unique=True, nullable=False)
            telefone = db.Column(db.String(100))
        cliente = ClienteBanco.query.get(id)
        return cliente
    
    def editar_cliente(self,cliente,id,db):
        if 'ClienteBanco' not in globals():
            class ClienteBanco(db.Model):
                __tablename__ = 'clientes'
                __table_args__ = {'extend_existing': True}
                id = db.Column(db.Integer, primary_key=True, autoincrement=True)
                nome = db.Column(db.String(100), nullable=False)
                sobrenome = db.Column(db.String(100), nullable=False)
                cpf = db.Column(db.String(100), unique=True)
                email = db.Column(db.String(100), unique=True, nullable=False)
                telefone = db.Column(db.String(100))
                data_nascimento = db.Column(db.Date)

            
        try:
            cliente_id = id
            cliente_banco = db.session.query(ClienteBanco).filter_by(id=cliente_id).first()

            if cliente_banco:
                cliente_banco.nome = cliente.nome
                cliente_banco.sobrenome = cliente.sobrenome
                cliente_banco.email = cliente.email
                cliente_banco.telefone = cliente.telefone
                cliente_banco.data_nascimento = cliente.data_nascimento
                cliente_banco.cpf = cliente.cpf_cliente

                db.session.commit()
                return str(f"Cliente atualizado com sucesso id: {cliente_banco.id}")
            else:
                return str(f"Cliente com id {cliente_id} não encontrado")
        except Exception as e:
            db.session.rollback()
            return str(f"Erro ao atualizar o cliente: {str(e)}")
        
    def renderizar_formulario(self):
        return render_template("cliente_form.html")


cliente_controller = ClienteController()
