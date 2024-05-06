from flask import render_template
from app.models.cliente import Cliente

class ClienteController:
    def cadastrar(self,cliente):
        cliente = cliente
        return str(cliente)

    def renderizar_formulario(self):
        return render_template("cliente_form.html")

cliente_controller = ClienteController()
