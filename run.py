from flask import Flask, request, render_template, redirect, url_for
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
            return redirect(url_for('cadastrar_cliente_view', erro="Email inválido! Por favor, forneça um email válido."))
        resultado = cliente_controller.cadastrar(cliente=cliente,db=db)
        return resultado
    else:
        return cliente_controller.renderizar_formulario()


if __name__ == '__main__':
    app.run(debug=True)
