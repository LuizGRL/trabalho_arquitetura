from flask import Flask, request, render_template, redirect, url_for,flash
from app.models.cliente import Cliente
from app.controllers.cliente_controller import ClienteController
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='app/views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/padroesAq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cliente_controller = ClienteController()

@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente_view():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        data_nascimento = request.form.get('data_nascimento')
        cpf = request.form.get('cpf')
        cliente = Cliente(nome=nome, telefone=telefone,sobrenome=sobrenome,data_nascimento=data_nascimento)
        cliente.set_email(email=email)
        cliente.set_cpf(cpf_cliente=cpf)
        if cliente.email is None or cliente.cpf_cliente is None:
            return render_template('error.html', message="Email ou cpf nulo")
        resultado = cliente_controller.cadastrar(cliente=cliente,db=db)
        if "sucesso" in resultado['message']:
            return render_template('home.html')
        else:
            return render_template('error.html', message=resultado["message"])

    else:
        return cliente_controller.renderizar_formulario()

@app.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    clientes = cliente_controller.listar_cliente(db)
    return render_template('cliente_lista.html', clientes=clientes)

@app.route('/editar_cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = cliente_controller.obter_cliente_por_id(id=id,db=db)
    if request.method == 'POST':
        if cliente:
            id = cliente.id
            nome = request.form.get('nome')
            sobrenome = request.form.get('sobrenome')
            email = request.form.get('email')
            telefone = request.form.get('telefone')
            data_nascimento = request.form.get('data_nascimento')
            cpf = request.form.get('cpf')
            cliente = Cliente(nome=nome, telefone=telefone,sobrenome=sobrenome,data_nascimento=data_nascimento)
            cliente.set_email(email=email)
            cliente.set_cpf(cpf_cliente=cpf)
            if cliente.email is None or cliente.cpf_cliente is None:
                return "email ou cpf em padrão incorreto", 404
            cliente_controller.editar_cliente(db=db,cliente=cliente,id=id)
            return redirect(url_for('listar_clientes'))
        else:
            return render_template('error.html', message="cliente não econtrado")

    else:
        if cliente:
            return render_template('cliente_edicao.html', cliente=cliente)
        else:
            return render_template('error.html', message="cliente não econtrado")

@app.route('/excluir_cliente/<int:id>')
def excluir_cliente(id):
    resultado = cliente_controller.excluir_cliente(id=id, db=db)
    
    if resultado["status"] == "not_found":
        return render_template('error.html', message=resultado["message"])
    elif resultado["status"] == "success":
        return render_template('cliente_lista.html', clientes=resultado["clientes"])
    else:
        return render_template('error.html', message=resultado["message"])


@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
