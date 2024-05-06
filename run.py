from flask import Flask, request, render_template, redirect, url_for
from app.models.cliente import Cliente
from app.controllers.cliente_controller import ClienteController
# from app.controllers.produto_controller import produto_controller

app = Flask(__name__,template_folder='app/views')
cliente_controller = ClienteController()
@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente_view():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        data_nascimento = request.form.get('data_nascimento')
        cliente = Cliente(nome=nome, telefone=telefone,sobrenome=sobrenome,data_nascimento=data_nascimento)
        cliente.set_email(email=email)
        if cliente.email is None:
            return redirect(url_for('cadastrar_cliente_view', erro="Email inválido! Por favor, forneça um email válido."))
        resultado = cliente_controller.cadastrar(cliente=cliente)
        return resultado
    else:
        return cliente_controller.renderizar_formulario()

# @app.route('/cadastrar_produto', methods=['GET', 'POST'])
# def cadastrar_produto_view():
#     if request.method == 'POST':
#         nome = request.form.get('nome')
#         preco = request.form.get('preco')
#         resultado = produto_controller.cadastrar(nome, preco)
#         return resultado
#     else:
#         return produto_controller.renderizar_formulario()

if __name__ == '__main__':
    app.run(debug=True)
